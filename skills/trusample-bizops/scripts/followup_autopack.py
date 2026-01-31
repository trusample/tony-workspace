#!/usr/bin/env python3
"""Generate a tailored follow-up pack for an opportunity.

Draft-only.

Creates:
- T+24h / T+3d / T+7d email drafts
- Optional objection-focused variants (price, lead time, docs)

Usage:
  python3 followup_autopack.py --lead "Acme Lab" --context "Synthetic CSF quote" --total "$1,250" --lead_time "2 weeks" --docs "COA/spec" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lead", default="(Lead name)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--email", default="")
    ap.add_argument("--context", default="(what they requested)")
    ap.add_argument("--total", default="")
    ap.add_argument("--lead_time", default="")
    ap.add_argument("--docs", default="")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    hi = f"Hi {args.contact}," if args.contact else f"Hi {args.lead},"

    summary_bits = []
    if args.total:
        summary_bits.append(f"Total: {args.total}")
    if args.lead_time:
        summary_bits.append(f"Lead time: {args.lead_time}")
    if args.docs:
        summary_bits.append(f"Docs: {args.docs}")
    summary = (" (" + "; ".join(summary_bits) + ")") if summary_bits else ""

    plan = dedent(
        f"""
        FOLLOW-UP PACK
        Lead: {args.lead}
        Email: {args.email or '(n/a)'}
        Context: {args.context}{summary}

        Recommended cadence:
        - T+24h: gentle bump + confirm any missing specs
        - T+3d: value add (docs/traceability/customization) + reconfirm lead time
        - T+7d: close the loop + offer quick call
        """
    ).strip()

    t24_subject = f"Quick follow-up — {args.context}"
    t24 = f"""{hi}

Just checking in on {args.context}{summary}. If you confirm ship-to + required storage/shipping temperature, we can finalize the quote and timeline.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    t3_subject = f"Docs + timeline — {args.context}"
    t3 = f"""{hi}

Sharing a quick note in case helpful: we can provide COA/spec documentation per lot and support custom formulations/packaging when needed. If you have a hard deadline, share the date and we’ll propose the fastest feasible option.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    t7_subject = f"Closing the loop — {args.context}"
    t7 = f"""{hi}

Wanted to close the loop on {args.context}. Are you still moving forward, or should I circle back at a better time?

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    # objection variants
    price_variant = f"""{hi}

If pricing is the blocker, tell me your target quantity/tiers and we’ll quote the best option. Many teams find the cost is offset by fewer repeats and tighter consistency.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    lead_variant = f"""{hi}

If timeline is the blocker, share your hard deadline and ship-to. We’ll confirm the fastest feasible lead time and the best shipping temperature option.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    docs_variant = f"""{hi}

If your QA/procurement team needs specific documentation (COA/spec/SDS or vendor packet), tell me the exact format/requirements and we’ll align.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    print(plan)
    print("\nT+24h SUBJECT:\n" + t24_subject)
    print("\nT+24h EMAIL:\n" + t24.strip())
    print("\nT+3d SUBJECT:\n" + t3_subject)
    print("\nT+3d EMAIL:\n" + t3.strip())
    print("\nT+7d SUBJECT:\n" + t7_subject)
    print("\nT+7d EMAIL:\n" + t7.strip())

    print("\n---\nOBJECTION VARIANTS")
    print("\nPRICE:\n" + price_variant.strip())
    print("\nLEAD TIME:\n" + lead_variant.strip())
    print("\nDOCS/QA:\n" + docs_variant.strip())


if __name__ == "__main__":
    main()
