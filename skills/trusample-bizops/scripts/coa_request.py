#!/usr/bin/env python3
"""Generate COA/spec sheet request template.

Draft-only.

Usage:
  python3 coa_request.py --product "Synthetic CSF" --lot "TS-2026-001" --recipient "Lab Manager" 
"""

import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", default="(Product/SKU)")
    ap.add_argument("--lot", default="(Lot ID if known)")
    ap.add_argument("--recipient", default="")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    hi = f"Hi {args.recipient}," if args.recipient else "Hi," 
    subject = f"COA / spec sheet request — {args.product} {('(' + args.lot + ')') if args.lot and args.lot != '(Lot ID if known)' else ''}".strip()

    body = f"""{hi}

Could you please share the COA and/or spec sheet for the following TruSample material?

- Product: {args.product}
- Lot: {args.lot}

If there are multiple documentation options (COA vs spec vs SDS), please include what’s available for this SKU.

Thank you,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    print("SUBJECT:\n" + subject)
    print("\nEMAIL DRAFT:\n" + body.strip())

if __name__ == "__main__":
    main()
