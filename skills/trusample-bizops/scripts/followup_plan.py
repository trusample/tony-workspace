#!/usr/bin/env python3
"""Generate a follow-up plan + message templates for a lead.

Draft-only.

Usage:
  python3 followup_plan.py --lead "Acme Lab" --context "Quote request for Synthetic CSF" --email "contact@acme.com" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lead", default="(Lead name)")
    ap.add_argument("--email", default="(lead email)")
    ap.add_argument("--context", default="(what they requested)")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    plan = dedent(f"""
    FOLLOW-UP PLAN (recommended)
    - T+24h: quick bump + offer help
    - T+3d: value add (documentation/COA, lead time, customization)
    - T+7d: close-the-loop (are they still interested? alternative timeline?)

    Lead: {args.lead}
    Email: {args.email}
    Context: {args.context}
    """).strip()

    t24_subject = f"Quick follow-up — {args.context}"
    t24 = f"""Hi {args.lead},

Just following up on {args.context}. Happy to help confirm specs (targets, concentrations, volume, storage) so we can finalize pricing and lead time.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    t3_subject = f"Documentation + lead time — {args.context}"
    t3 = f"""Hi {args.lead},

Sharing a quick note in case helpful: TruSample lots include clear lot IDs and can be provided with COA/spec documentation per SKU. We also support custom formulations when you need specific targets/concentrations.

If you share your ship-to and desired timeline, I’ll confirm lead time and pricing.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    t7_subject = f"Closing the loop — {args.context}"
    t7 = f"""Hi {args.lead},

Wanted to close the loop on {args.context}. Are you still moving forward, or should I circle back at a better time?

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


if __name__ == "__main__":
    main()
