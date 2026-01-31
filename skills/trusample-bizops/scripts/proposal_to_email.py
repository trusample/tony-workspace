#!/usr/bin/env python3
"""Convert a proposal markdown (from proposal_generator.py) into a sendable email.

Draft-only.

Input: --proposal (string) or stdin.
Output:
- Subject
- Email body (short, procurement-friendly)
- Optional: attach proposal as pasted section or reference

Usage:
  python3 proposal_to_email.py --proposal "$(cat proposal.md)" --customer "Acme Lab" --project "Synthetic CSF" 
  cat proposal.md | python3 proposal_to_email.py --customer "Acme Lab" --project "Synthetic CSF"
"""

import argparse
import re
import sys
from textwrap import dedent


def first_nonempty(lines):
    for l in lines:
        if l.strip():
            return l.strip()
    return ""


def extract_total(md: str):
    m = re.search(r"\*\*Total:\*\*\s*([^\n]+)", md)
    return m.group(1).strip() if m else ""


def extract_lead_time(md: str):
    m = re.search(r"Estimated lead time / delivery window:\s*([^\n]+)", md)
    return m.group(1).strip() if m else ""


def extract_ship_to(md: str):
    m = re.search(r"Ship-to:\s*([^\n]+)", md)
    return m.group(1).strip() if m else ""


def extract_scope_bullets(md: str):
    # Pull the “Material specification” bullets if present.
    block = ""
    m = re.search(r"\*\*Material specification\*\*([\s\S]+?)\*\*Handling & logistics\*\*", md)
    if m:
        block = m.group(1)
    lines = [l.rstrip() for l in block.splitlines()]
    bullets = [l.strip() for l in lines if l.strip().startswith("-")]
    return bullets[:6]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer", default="(Customer)")
    ap.add_argument("--project", default="(Project)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--proposal", default="")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    md = args.proposal
    if not md.strip():
        md = sys.stdin.read() if not sys.stdin.isatty() else ""

    if not md.strip():
        print("ERROR: Provide --proposal or pipe proposal markdown via stdin.")
        raise SystemExit(2)

    total = extract_total(md)
    lead = extract_lead_time(md)
    ship_to = extract_ship_to(md)
    bullets = extract_scope_bullets(md)

    subject = f"Quote — {args.project} ({args.customer})"

    hi = f"Hi {args.contact}," if args.contact else "Hi there,"

    scope_lines = "\n".join(bullets) if bullets else "(see attached/pasted proposal)"

    body = dedent(
        f"""{hi}

Attached is our quote/proposal for **{args.project}**.

Summary
{scope_lines}

Commercials
- Total: {total or '(see proposal)'}
- Lead time / delivery window: {lead or '(see proposal)'}
- Ship-to: {ship_to or '(confirm)'}

To proceed, please confirm:
1) Billing contact + billing address
2) Preferred invoice delivery method (PDF vs link)
3) PO number (if applicable)

Best,
TruSample
{args.from_email}
"""
    ).strip()

    print("SUBJECT:\n" + subject)
    print("\nEMAIL BODY:\n" + body)


if __name__ == "__main__":
    main()
