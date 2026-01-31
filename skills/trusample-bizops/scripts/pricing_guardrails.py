#!/usr/bin/env python3
"""Generate consistent pricing/terms/lead-time/shipping language blocks.

Draft-only. This is meant to keep outbound messaging consistent.

Usage:
  python3 pricing_guardrails.py --currency USD --terms "Net 15" --lead_time "2 weeks" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--currency", default="USD")
    ap.add_argument("--terms", default="Net 15")
    ap.add_argument("--validity", default="14 days")
    ap.add_argument("--lead_time", default="(confirm once specs are final)")
    ap.add_argument("--shipping", default="Shipping billed at cost; temperature control as required")
    ap.add_argument("--moq", default="(define per SKU / program)")
    ap.add_argument("--custom", default="Custom formulations quoted case-by-case after spec confirmation")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    blocks = dedent(
        f"""
        PRICING + COMMERCIAL GUARDRAILS (copy blocks)

        VALIDITY
        - This quote is valid for {args.validity} unless otherwise stated.

        PAYMENT TERMS
        - Payment terms: {args.terms}.

        LEAD TIME
        - Estimated lead time: {args.lead_time}. Lead time is confirmed once final specs are approved.

        MOQ
        - MOQ: {args.moq}.

        SHIPPING / HANDLING
        - {args.shipping}.

        CUSTOM WORK
        - {args.custom}.

        WHAT WE NEED TO INVOICE
        - Billing contact + billing address
        - Preferred invoice delivery method (PDF vs link)
        - PO number (if applicable)

        SIGNATURE
        TruSample
        {args.from_email}
        """
    ).strip()

    print(blocks)


if __name__ == "__main__":
    main()
