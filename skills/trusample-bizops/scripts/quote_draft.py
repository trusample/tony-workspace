#!/usr/bin/env python3
"""Generate a TruSample quote email draft + clarifying questions.

Draft-only: no sending.

Usage:
  python3 quote_draft.py --matrix "Synthetic CSF" --analytes "Aβ42, t-tau" --concentrations "100 pg/mL" --volume "10 mL" --units "20" --ship_to "US" --timeline "2 weeks" 

If args omitted, uses sensible placeholders.
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix", default="Synthetic Urine")
    ap.add_argument("--analytes", default="(please specify)")
    ap.add_argument("--concentrations", default="(please specify)")
    ap.add_argument("--volume", default="(e.g., 10 mL per unit)")
    ap.add_argument("--units", default="(e.g., 10 units)")
    ap.add_argument("--ship_to", default="(country + ZIP/postal)")
    ap.add_argument("--timeline", default="(desired delivery date)")
    ap.add_argument("--use_case", default="assay validation / method development")
    ap.add_argument("--contact_name", default="")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    name_line = f"Hi {args.contact_name}," if args.contact_name else "Hi there," 

    subject = f"Quote request — {args.matrix} ({args.use_case})"

    body = f"""{name_line}

Thanks for reaching out to TruSample. We can provide an ISO 13485 certified lot of {args.matrix} tailored for {args.use_case}.

To quote accurately (pricing + lead time), can you confirm the details below?

Requested material
- Matrix: {args.matrix}
- Targets/analytes: {args.analytes}
- Target concentrations: {args.concentrations}
- Fill volume per unit: {args.volume}
- Quantity: {args.units}
- Ship-to: {args.ship_to}
- Target timeline: {args.timeline}

A few quick clarifying questions (so we match your workflow)
1) Storage/handling requirements (ambient / 2–8°C / -20°C / -80°C)?
2) Any required additives (preservatives, protein, surfactants) or constraints?
3) Format preference (single lot vs. multiple lots; aliquoted vs bulk)?
4) Do you need a COA/spec sheet with each lot (default: available per SKU)?

Once we have these, we’ll reply with a quote and a lead-time estimate.

Best,
TruSample
{args.from_email}
"""

    assumptions = dedent("""
    ASSUMPTIONS / NOTES
    - Draft-only template. Replace placeholders with actual specs.
    - ISO 13485 certified statement should match your certification scope.
    - Add MOQ/lead-time guidance once you define it.
    """).strip()

    internal = dedent(f"""
    INTERNAL SUMMARY (copy/paste into CRM)
    - Request: {args.matrix}
    - Use case: {args.use_case}
    - Analytes: {args.analytes}
    - Concentrations: {args.concentrations}
    - Volume/unit: {args.volume}
    - Units: {args.units}
    - Ship-to: {args.ship_to}
    - Timeline: {args.timeline}
    - Next: ask storage/additives/format/COA needs
    """).strip()

    print("SUBJECT:\n" + subject)
    print("\nEMAIL DRAFT:\n" + body.strip())
    print("\n" + assumptions)
    print("\n" + internal)


if __name__ == "__main__":
    main()
