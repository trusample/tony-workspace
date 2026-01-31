#!/usr/bin/env python3
"""Turn an inbound email/thread into a structured opportunity card.

Draft-only.

Input: paste email/text via --text (or stdin)
Output:
- Opportunity card (who/what/when/risks)
- Suggested next actions
- Suggested reply (short)

Usage:
  python3 customer_intake_summary.py --text "<paste thread>"
  pbpaste | python3 customer_intake_summary.py
"""

import argparse
import re
import sys
from textwrap import dedent


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip())


def pick(patterns, text):
    for pat in patterns:
        m = re.search(pat, text, flags=re.I)
        if m:
            for g in m.groups():
                if g and g.strip():
                    return norm(g)
    return ""


def extract(text: str):
    # best effort: email, org, name, phone
    email = pick([r"\b([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,})\b"], text)
    phone = pick([r"(\+?1?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})"], text)

    # crude signature detection
    name = pick(
        [
            r"(?m)^\s*Best,\s*$\n\s*([A-Za-z][A-Za-z .'-]{1,40})\b",
            r"(?m)^\s*Regards,\s*$\n\s*([A-Za-z][A-Za-z .'-]{1,40})\b",
            r"(?m)^\s*Thanks,\s*$\n\s*([A-Za-z][A-Za-z .'-]{1,40})\b",
        ],
        text,
    )
    if name:
        name = name.strip("-–• ")

    org = pick(
        [
            r"company\s*[:\-]\s*([^\n\r]+)",
            r"organization\s*[:\-]\s*([^\n\r]+)",
        ],
        text,
    )
    if not org:
        # signature-style org line between name and email
        m = re.search(
            r"(?m)^\s*[A-Za-z][A-Za-z .'-]{1,40}\s*$\n\s*([A-Z][A-Za-z0-9&.,' -]{2,60})\s*$\n\s*[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
            text,
            flags=re.I,
        )
        if m:
            org = norm(m.group(1))

    # high-level intent
    intent = ""
    if re.search(r"\bquote\b|\bpricing\b|\bhow much\b", text, flags=re.I):
        intent = "Quote / pricing"
    elif re.search(r"\bsample\b|\bmaterial\b|\bavailability\b", text, flags=re.I):
        intent = "Availability / sample request"
    elif re.search(r"\bdistributor\b|\bpartnership\b", text, flags=re.I):
        intent = "Partnership / distribution"
    else:
        intent = "General inquiry"

    # urgency
    urgency = pick([r"within\s+([0-9]+\s*(?:days?|weeks?|months?))", r"need\s*(?:by)?\s*[:\-]?\s*([^\n\r]+)"], text)

    # pull potential product mentions
    products = []
    for token in ["Synthetic CSF", "Synthetic Urine", "Synthetic Plasma", "Synthetic Serum", "PT", "proficiency testing", "QC", "controls"]:
        if re.search(re.escape(token), text, flags=re.I):
            products.append(token)

    # constraints
    constraints = []
    for kw in ["-80", "-20", "2-8", "ambient", "dry ice", "COA", "SDS", "spec", "aliquot", "bulk", "custom"]:
        if re.search(rf"\b{re.escape(kw)}\b", text, flags=re.I):
            constraints.append(kw)

    return {
        "contact_name": name,
        "contact_email": email,
        "contact_phone": phone,
        "organization": org,
        "intent": intent,
        "urgency": urgency,
        "product_signals": ", ".join(products) if products else "(not specified)",
        "constraints": ", ".join(constraints) if constraints else "(none detected)",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default="")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    text = args.text
    if not text.strip():
        text = sys.stdin.read() if not sys.stdin.isatty() else ""

    if not text.strip():
        print("ERROR: Provide --text or pipe input.")
        raise SystemExit(2)

    info = extract(text)

    card = dedent(
        f"""
        OPPORTUNITY CARD
        - Organization: {info['organization'] or '(unknown)'}
        - Contact: {info['contact_name'] or '(unknown)'}
        - Email: {info['contact_email'] or '(unknown)'}
        - Phone: {info['contact_phone'] or '(unknown)'}
        - Intent: {info['intent']}
        - Urgency: {info['urgency'] or '(not stated)'}
        - Product signals: {info['product_signals']}
        - Constraints/docs: {info['constraints']}

        RISKS / UNKNOWN
        - Specs may be incomplete (targets/concentrations/volume/qty/ship-to)
        - Qualification requirements (vendor packet, docs) unknown

        NEXT ACTIONS (recommended)
        1) Confirm specs: matrix, targets/analytes, concentrations, volume/unit, quantity
        2) Confirm logistics: ship-to, storage/shipping temp, deadline
        3) Confirm docs: COA/spec/SDS + required format
        4) Provide quote + lead time OR propose a 10–15 min call
        """
    ).strip()

    # short reply template
    hi = f"Hi {info['contact_name']}," if info["contact_name"] else "Hi there,"
    reply = f"""{hi}

Thanks for reaching out — happy to help. To quote accurately and confirm lead time, can you share:
- matrix + targets/analytes + target concentrations
- volume per unit + quantity
- ship-to + required storage/shipping temp + desired delivery date
- any documentation needs (COA/spec/SDS)

Once we have that, we’ll reply with pricing and lead time.

Best,
TruSample
{args.from_email}
"""

    print(card)
    print("\nSUGGESTED REPLY (short)\n" + reply.strip())


if __name__ == "__main__":
    main()
