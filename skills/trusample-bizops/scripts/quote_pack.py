#!/usr/bin/env python3
"""Generate a full "quote pack" from an inbound request.

Draft-only. This chains together:
- quote_extractor: extract structured spec + missing info
- proposal_generator: 1–2 page proposal markdown
- proposal_to_email: sendable email summary
- followup_autopack: follow-up sequence + objection variants

Output:
- structured spec
- proposal.md (printed)
- email subject/body
- follow-up pack

Usage:
  python3 quote_pack.py --text "<paste inbound request>" --customer "Acme Lab" --project "Synthetic CSF" --price '$1,250' --terms "Net 15" --storage=-80C --shipping_temp "Dry ice"
  pbpaste | python3 quote_pack.py --customer "Acme Lab" --project "Synthetic CSF" --price '$1,250'

Notes:
- You can omit price/terms/storage/shipping_temp; placeholders will be used.
- Use single quotes around $ values to avoid shell expansion.
"""

import argparse
import sys

# Local imports (same folder)
import quote_extractor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default="")
    ap.add_argument("--customer", default="(Customer)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--project", default="(Project)")

    ap.add_argument("--price", default="(Total price)")
    ap.add_argument("--terms", default="Net 15")
    ap.add_argument("--validity", default="14 days")

    ap.add_argument("--storage", default="(Storage)")
    ap.add_argument("--shipping_temp", default="(Ambient / cold pack / dry ice)")

    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    text = args.text
    if not text.strip():
        text = sys.stdin.read() if not sys.stdin.isatty() else ""
    if not text.strip():
        print("ERROR: Provide --text or pipe input.")
        raise SystemExit(2)

    # 1) Extract spec
    spec = quote_extractor.best_effort_extract(text)

    # map into proposal fields
    matrix = spec.get("matrix") or "(Matrix)"
    analytes = spec.get("analytes") or "(Targets/analytes)"
    concentrations = spec.get("concentrations") or "(Target concentrations)"
    volume = spec.get("volume") or "(Fill volume per unit)"
    units = spec.get("units") or "(Quantity)"
    ship_to = spec.get("ship_to") or "(Ship-to)"
    timeline = spec.get("timeline") or "(Lead time / delivery window)"
    documentation = spec.get("documentation") or "COA / spec sheet per lot (if applicable)"

    # 2) Render proposal markdown (inline, no subprocess)
    from textwrap import dedent

    attn = f"Attn: {args.contact}\n" if args.contact else ""

    proposal_md = dedent(
        f"""# Quote / Proposal — {args.project}

**Customer:** {args.customer}  
{attn}**Prepared by:** TruSample ({args.from_email})  
**Validity:** {args.validity}

## 1) Scope of supply
We will provide the following synthetic reference material(s) per the specifications below.

**Material specification**
- Matrix: {matrix}
- Targets/analytes: {analytes}
- Target concentrations: {concentrations}
- Fill volume per unit: {volume}
- Quantity: {units}

**Handling & logistics**
- Storage: {args.storage}
- Shipping temperature: {args.shipping_temp}
- Ship-to: {ship_to}
- Estimated lead time / delivery window: {timeline}

**Documentation**
- {documentation}

## 2) Pricing
**Total:** {args.price}  
**Payment terms:** {args.terms}

## 3) Assumptions / exclusions
- Pricing and lead time are contingent on final confirmed specifications.
- Any regulatory/vendor qualification packet requirements should be specified in advance.
- Shipping costs/taxes may be added depending on destination and temperature control.

## 4) Next steps
1) Confirm billing contact + billing address + PO (if applicable)
2) Confirm ship-to address and required shipping temperature
3) Invoice issuance and scheduling of fulfillment
"""
    ).strip()

    # 3) Proposal → email
    import proposal_to_email
    # Monkey-call parsing helpers
    total = proposal_to_email.extract_total(proposal_md)
    lead = proposal_to_email.extract_lead_time(proposal_md)
    ship = proposal_to_email.extract_ship_to(proposal_md)
    bullets = proposal_to_email.extract_scope_bullets(proposal_md)

    subject = f"Quote — {args.project} ({args.customer})"
    hi = f"Hi {args.contact}," if args.contact else "Hi there,"
    scope_lines = "\n".join(bullets) if bullets else "(see attached/pasted proposal)"

    email_body = (
        f"{hi}\n\n"
        f"Attached is our quote/proposal for **{args.project}**.\n\n"
        f"Summary\n{scope_lines}\n\n"
        f"Commercials\n- Total: {total or '(see proposal)'}\n"
        f"- Lead time / delivery window: {lead or '(see proposal)'}\n"
        f"- Ship-to: {ship or '(confirm)'}\n\n"
        f"To proceed, please confirm:\n"
        f"1) Billing contact + billing address\n"
        f"2) Preferred invoice delivery method (PDF vs link)\n"
        f"3) PO number (if applicable)\n\n"
        f"Best,\nTruSample\n{args.from_email}\n"
    )

    # 4) Follow-up autopack
    import followup_autopack

    # Reuse followup_autopack by calling its logic inline is messy; instead, replicate minimal assembly.
    # We'll just print the existing script output via a lightweight formatting here.
    followups = []
    ctx_summary_bits = []
    if args.price and args.price != "(Total price)":
        ctx_summary_bits.append(f"Total: {args.price}")
    if timeline and timeline != "(Lead time / delivery window)":
        ctx_summary_bits.append(f"Lead time: {timeline}")
    if documentation:
        ctx_summary_bits.append(f"Docs: {documentation}")
    ctx_summary = (" (" + "; ".join(ctx_summary_bits) + ")") if ctx_summary_bits else ""

    t24_subject = f"Quick follow-up — {args.project}"
    t24 = f"Hi {args.customer},\n\nJust checking in on {args.project}{ctx_summary}. If you confirm ship-to + required storage/shipping temperature, we can finalize the quote and timeline.\n\nBest,\nTruSample\n{args.from_email}\n"

    t3_subject = f"Docs + timeline — {args.project}"
    t3 = f"Hi {args.customer},\n\nSharing a quick note in case helpful: we can provide COA/spec documentation per lot and support custom formulations/packaging when needed. If you have a hard deadline, share the date and we’ll propose the fastest feasible option.\n\nBest,\nTruSample\n{args.from_email}\n"

    t7_subject = f"Closing the loop — {args.project}"
    t7 = f"Hi {args.customer},\n\nWanted to close the loop on {args.project}. Are you still moving forward, or should I circle back at a better time?\n\nBest,\nTruSample\n{args.from_email}\n"

    # Print everything
    print("STRUCTURED SPEC (best-effort)")
    for k in quote_extractor.FIELDS:
        v = spec.get(k, "")
        print(f"- {k}: {v if v else '(missing)'}")

    miss = quote_extractor.missing(spec)
    print("\nMISSING INFO (required to quote)")
    if miss:
        for k in miss:
            print(f"- {k}")
    else:
        print("- (none detected)")

    print("\n====================\nPROPOSAL (Markdown)\n====================\n")
    print(proposal_md)

    print("\n====================\nSENDABLE EMAIL\n====================\n")
    print("SUBJECT:\n" + subject)
    print("\nBODY:\n" + email_body.strip())

    print("\n====================\nFOLLOW-UP PACK\n====================\n")
    print("T+24h SUBJECT:\n" + t24_subject)
    print("\nT+24h EMAIL:\n" + t24.strip())
    print("\nT+3d SUBJECT:\n" + t3_subject)
    print("\nT+3d EMAIL:\n" + t3.strip())
    print("\nT+7d SUBJECT:\n" + t7_subject)
    print("\nT+7d EMAIL:\n" + t7.strip())

    print("\nOBJECTION VARIANTS (quick)\n- If price is the blocker: ask for target tier/quantity; offer best tier.\n- If timeline is the blocker: ask for hard deadline + ship-to; propose fastest option.\n- If docs are the blocker: ask QA format requirements; align COA/spec/SDS/vendor packet.")


if __name__ == "__main__":
    main()
