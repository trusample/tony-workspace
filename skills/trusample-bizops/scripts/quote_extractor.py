#!/usr/bin/env python3
"""Extract a structured quote spec from a messy inbound request.

Draft-only.

Input: paste email/text via --text (or stdin).
Output:
- Structured spec fields (best-effort)
- Missing info checklist
- Recommended next email draft (pulls from quote_draft logic)
- CRM-ready summary

Usage:
  python3 quote_extractor.py --text "<paste message>"
  pbpaste | python3 quote_extractor.py
"""

import argparse
import re
from textwrap import dedent


FIELDS = [
    "matrix",
    "analytes",
    "concentrations",
    "volume",
    "units",
    "ship_to",
    "timeline",
    "storage",
    "format",
    "documentation",
]


def norm(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s


def pick(patterns, text):
    for pat in patterns:
        m = re.search(pat, text, flags=re.I)
        if m:
            # return first non-empty group
            for g in m.groups():
                if g and g.strip():
                    return norm(g)
    return ""


def best_effort_extract(text: str):
    t = text

    matrix = pick(
        [
            r"matrix\s*[:\-]\s*([^\n\r]+)",
            r"sample\s*matrix\s*[:\-]\s*([^\n\r]+)",
            r"synthetic\s+(csf|urine|plasma|serum|saliva)\b",
        ],
        t,
    )
    if matrix and matrix.lower() in ["csf", "urine", "plasma", "serum", "saliva"]:
        matrix = f"Synthetic {matrix.upper() if matrix.lower() == 'csf' else matrix.title()}"

    analytes = pick(
        [
            r"analytes?\s*[:\-]\s*([^\n\r]+)",
            r"targets?\s*[:\-]\s*([^\n\r]+)",
            r"biomarkers?\s*[:\-]\s*([^\n\r]+)",
        ],
        t,
    )
    if not analytes:
        # best-effort: common biomarker tokens in free text
        toks = re.findall(r"\b(?:Aβ\s*\d+|Abeta\s*\d+|Amyloid\s*beta\s*\d+|t-?tau|p-?tau\s*\d*|NfL|GFAP)\b", t, flags=re.I)
        if toks:
            analytes = ", ".join(dict.fromkeys([norm(x) for x in toks]))

    concentrations = pick(
        [
            r"concentrations?\s*[:\-]\s*([^\n\r]+)",
            r"levels?\s*[:\-]\s*([^\n\r]+)",
            r"(?:at|around)\s+([0-9]+\s*(?:ng\/mL|pg\/mL|ug\/mL|mg\/mL|uM|nM|mM))",
        ],
        t,
    )

    volume = pick(
        [
            r"(?:fill\s*)?volume\s*[:\-]\s*([^\n\r]+)",
            r"([0-9]+\s*(?:uL|µL|mL|L))\s*(?:per\s*(?:vial|unit|tube))?",
        ],
        t,
    )

    units = pick(
        [
            r"quantity\s*[:\-]\s*([^\n\r]+)",
            r"qty\s*[:\-]\s*([^\n\r]+)",
            r"(?:need|request(?:ing)?|looking\s*for)\s+([0-9]+\s*(?:vials|units|tubes|bottles|samples))",
            r"\b([0-9]+)\s*(vials|units|tubes|bottles|samples)\b",
        ],
        t,
    )

    ship_to = pick(
        [
            r"ship(?:\s*to)?\s*[:\-]\s*([^\n\r]+)",
            r"deliver(?:\s*to)?\s*[:\-]\s*([^\n\r]+)",
            r"address\s*[:\-]\s*([^\n\r]+)",
            r"\bship\s*to\s*([0-9]{5}(?:-[0-9]{4})?)\b",
            r"\bto\s*([0-9]{5}(?:-[0-9]{4})?)\b",
        ],
        t,
    )

    timeline = pick(
        [
            r"within\s+([0-9]+\s*(?:days?|weeks?|months?))",
            r"by\s+([A-Za-z]{3,9}\s+\d{1,2}(?:,\s*\d{4})?)",
            r"timeline\s*[:\-]\s*([^\n\r]+)",
            r"need\s*(?:by)?\s*[:\-]?\s*([^\n\r]+)",
        ],
        t,
    )
    # avoid misclassifying documentation words as timeline
    if timeline and re.search(r"\b(COA|spec|SDS)\b", timeline, flags=re.I):
        timeline = ""

    storage = pick(
        [
            r"storage\s*[:\-]\s*([^\n\r]+)",
            r"(-?\d+\s*°?\s*C)\b",
            r"(ambient|room\s*temp|2\s*[-–]\s*8\s*°?\s*C|-20\s*°?\s*C|-80\s*°?\s*C)\b",
        ],
        t,
    )

    fmt = pick(
        [
            r"format\s*[:\-]\s*([^\n\r]+)",
            r"(aliquoted|aliquots?|bulk|vials?)\b",
        ],
        t,
    )

    documentation = pick(
        [
            r"docs?\s*[:\-]\s*([^\n\r]+)",
            r"documentation\s*[:\-]\s*([^\n\r]+)",
            r"(COA|spec\s*sheet|SDS)\b",
        ],
        t,
    )

    return {
        "matrix": matrix,
        "analytes": analytes,
        "concentrations": concentrations,
        "volume": volume,
        "units": units,
        "ship_to": ship_to,
        "timeline": timeline,
        "storage": storage,
        "format": fmt,
        "documentation": documentation,
    }


def missing(spec: dict):
    required = ["matrix", "analytes", "concentrations", "volume", "units", "ship_to", "timeline"]
    missing = [k for k in required if not spec.get(k)]
    return missing


def render_next_email(spec: dict, from_email: str = "info@trusample.bio"):
    # Use the same structure as quote_draft.py but keep it in this file for portability.
    matrix = spec.get("matrix") or "(Matrix)"
    analytes = spec.get("analytes") or "(please specify)"
    concentrations = spec.get("concentrations") or "(please specify)"
    volume = spec.get("volume") or "(e.g., 10 mL per unit)"
    units = spec.get("units") or "(e.g., 10 units)"
    ship_to = spec.get("ship_to") or "(country + ZIP/postal)"
    timeline = spec.get("timeline") or "(desired delivery date)"

    subject = f"Re: Quote — {matrix}"

    body = f"""Hi there,

Thanks for reaching out to TruSample — happy to help.

To quote accurately (pricing + lead time), can you confirm the details below?

Requested material
- Matrix: {matrix}
- Targets/analytes: {analytes}
- Target concentrations: {concentrations}
- Fill volume per unit: {volume}
- Quantity: {units}
- Ship-to: {ship_to}
- Target timeline: {timeline}

A few quick clarifying questions (so we match your workflow)
1) Storage/handling requirements (ambient / 2–8°C / -20°C / -80°C)?
2) Any required additives (preservatives, protein, surfactants) or constraints?
3) Format preference (single lot vs. multiple lots; aliquoted vs bulk)?
4) Do you need a COA/spec sheet with each lot?

Once we have these, we’ll reply with a quote and a lead-time estimate.

Best,
TruSample
{from_email}
"""

    return subject, body


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

    spec = best_effort_extract(text)
    miss = missing(spec)

    print("STRUCTURED SPEC (best-effort)")
    for k in FIELDS:
        v = spec.get(k, "")
        print(f"- {k}: {v if v else '(missing)'}")

    print("\nMISSING INFO (required to quote)")
    if miss:
        for k in miss:
            print(f"- {k}")
    else:
        print("- (none detected)")

    subj, body = render_next_email(spec, args.from_email)
    print("\nRECOMMENDED NEXT EMAIL")
    print("SUBJECT:\n" + subj)
    print("\nBODY:\n" + body.strip())

    crm = dedent(
        f"""
        CRM SUMMARY
        - Matrix: {spec.get('matrix') or 'TBD'}
        - Analytes: {spec.get('analytes') or 'TBD'}
        - Concentrations: {spec.get('concentrations') or 'TBD'}
        - Volume/unit: {spec.get('volume') or 'TBD'}
        - Units: {spec.get('units') or 'TBD'}
        - Ship-to: {spec.get('ship_to') or 'TBD'}
        - Timeline: {spec.get('timeline') or 'TBD'}
        - Storage: {spec.get('storage') or 'TBD'}
        - Format: {spec.get('format') or 'TBD'}
        - Docs: {spec.get('documentation') or 'TBD'}
        - Next: request missing info + confirm feasibility/lead time
        """
    ).strip()

    print("\n" + crm)


if __name__ == "__main__":
    import sys
    main()
