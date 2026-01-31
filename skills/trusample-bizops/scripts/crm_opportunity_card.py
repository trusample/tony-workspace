#!/usr/bin/env python3
"""Generate a CRM-ready opportunity card (JSON + human summary).

Draft-only.

Usage:
  python3 crm_opportunity_card.py --customer "Acme Lab" --source "email" --stage "New" \
    --request "Synthetic CSF Aβ42" --value "1250" --currency "USD"
"""

import argparse
import json
from datetime import datetime, timezone


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer", default="(Customer)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--email", default="")
    ap.add_argument("--source", default="email")
    ap.add_argument("--stage", default="New")
    ap.add_argument("--request", default="(Request summary)")
    ap.add_argument("--value", default="")
    ap.add_argument("--currency", default="USD")
    ap.add_argument("--notes", default="")
    args = ap.parse_args()

    card = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "customer": args.customer,
        "contact": args.contact,
        "email": args.email,
        "source": args.source,
        "stage": args.stage,
        "request": args.request,
        "value": args.value,
        "currency": args.currency,
        "notes": args.notes,
    }

    print("HUMAN SUMMARY")
    print(f"- Customer: {args.customer}")
    if args.contact:
        print(f"- Contact: {args.contact}")
    if args.email:
        print(f"- Email: {args.email}")
    print(f"- Source: {args.source}")
    print(f"- Stage: {args.stage}")
    print(f"- Request: {args.request}")
    if args.value:
        print(f"- Value: {args.value} {args.currency}")
    if args.notes:
        print(f"- Notes: {args.notes}")

    print("\nJSON")
    print(json.dumps(card, indent=2))


if __name__ == "__main__":
    main()
