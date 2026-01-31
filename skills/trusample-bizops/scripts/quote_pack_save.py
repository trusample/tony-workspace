#!/usr/bin/env python3
"""Run quote_pack and save outputs to a timestamped folder.

Draft-only.

Creates:
- spec.txt
- proposal.md
- email.txt
- followups.txt

Usage:
  python3 quote_pack_save.py --customer "Acme Lab" --project "Synthetic CSF" --price '$1,250' --storage=-80C --shipping_temp "Dry ice" --text "..."
"""

import argparse
import os
from datetime import datetime

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
    ap.add_argument("--outdir", default="out/quote-packs")
    args = ap.parse_args()

    text = args.text
    if not text.strip():
        import sys
        text = sys.stdin.read() if not sys.stdin.isatty() else ""
    if not text.strip():
        raise SystemExit("ERROR: Provide --text or pipe input.")

    spec = quote_extractor.best_effort_extract(text)

    # reuse quote_pack by importing and calling via a tiny subprocess-free render
    from textwrap import dedent

    matrix = spec.get("matrix") or "(Matrix)"
    analytes = spec.get("analytes") or "(Targets/analytes)"
    concentrations = spec.get("concentrations") or "(Target concentrations)"
    volume = spec.get("volume") or "(Fill volume per unit)"
    units = spec.get("units") or "(Quantity)"
    ship_to = spec.get("ship_to") or "(Ship-to)"
    timeline = spec.get("timeline") or "(Lead time / delivery window)"
    documentation = spec.get("documentation") or "COA / spec sheet per lot (if applicable)"

    proposal_md = dedent(
        f"""# Quote / Proposal — {args.project}

**Customer:** {args.customer}  
**Prepared by:** TruSample ({args.from_email})  
**Validity:** {args.validity}

## 1) Scope of supply
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

## 3) Next steps
1) Confirm billing contact + billing address + PO (if applicable)
2) Confirm ship-to address and required shipping temperature
3) Invoice issuance and scheduling of fulfillment
"""
    ).strip() + "\n"

    # email (via proposal_to_email helpers)
    import proposal_to_email
    total = proposal_to_email.extract_total(proposal_md)
    lead = proposal_to_email.extract_lead_time(proposal_md)
    ship = proposal_to_email.extract_ship_to(proposal_md)
    bullets = proposal_to_email.extract_scope_bullets(proposal_md)

    subject = f"Quote — {args.project} ({args.customer})"
    hi = f"Hi {args.contact}," if args.contact else "Hi there,"
    scope_lines = "\n".join(bullets) if bullets else "(see attached/pasted proposal)"

    email_txt = (
        f"SUBJECT:\n{subject}\n\n"
        f"BODY:\n{hi}\n\n"
        f"Attached is our quote/proposal for {args.project}.\n\n"
        f"Summary\n{scope_lines}\n\n"
        f"Commercials\n- Total: {total or '(see proposal)'}\n"
        f"- Lead time / delivery window: {lead or '(see proposal)'}\n"
        f"- Ship-to: {ship or '(confirm)'}\n\n"
        f"To proceed, please confirm:\n1) Billing contact + billing address\n2) Invoice delivery (PDF vs link)\n3) PO number (if applicable)\n\n"
        f"Best,\nTruSample\n{args.from_email}\n"
    )

    followups_txt = (
        f"T+24h SUBJECT: Quick follow-up — {args.project}\n\n"
        f"Hi {args.customer},\n\nJust checking in on {args.project}. If you confirm ship-to + required storage/shipping temperature, we can finalize the quote and timeline.\n\nBest,\nTruSample\n{args.from_email}\n\n"
        f"T+3d SUBJECT: Docs + timeline — {args.project}\n\n"
        f"Hi {args.customer},\n\nWe can provide COA/spec documentation per lot and support custom formulations/packaging when needed. If you have a hard deadline, share the date and we’ll propose the fastest feasible option.\n\nBest,\nTruSample\n{args.from_email}\n\n"
        f"T+7d SUBJECT: Closing the loop — {args.project}\n\n"
        f"Hi {args.customer},\n\nWanted to close the loop on {args.project}. Are you still moving forward, or should I circle back at a better time?\n\nBest,\nTruSample\n{args.from_email}\n"
    )

    miss = quote_extractor.missing(spec)
    spec_txt = "STRUCTURED SPEC (best-effort)\n" + "\n".join(
        [f"- {k}: {spec.get(k) or '(missing)'}" for k in quote_extractor.FIELDS]
    )
    spec_txt += "\n\nMISSING INFO\n" + ("\n".join([f"- {m}" for m in miss]) if miss else "- (none detected)") + "\n"

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_customer = "".join([c for c in args.customer if c.isalnum() or c in ("-", "_")]).strip() or "customer"
    folder = os.path.join(args.outdir, f"{stamp}-{safe_customer}")
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "spec.txt"), "w", encoding="utf-8") as f:
        f.write(spec_txt)
    with open(os.path.join(folder, "proposal.md"), "w", encoding="utf-8") as f:
        f.write(proposal_md)
    with open(os.path.join(folder, "email.txt"), "w", encoding="utf-8") as f:
        f.write(email_txt)
    with open(os.path.join(folder, "followups.txt"), "w", encoding="utf-8") as f:
        f.write(followups_txt)

    print(f"Saved quote pack to: {folder}")


if __name__ == "__main__":
    main()
