#!/usr/bin/env python3
"""Generate distributor outreach drafts (email + LinkedIn + X DM).

Draft-only.

Usage:
  python3 outreach_draft.py --company "Acme Bio" --contact "Name" --angle "distributor" --products "Synthetic Urine, Synthetic CSF" --proof "ISO 13485 certified" 
"""

import argparse
from textwrap import dedent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", default="(Distributor Company)")
    ap.add_argument("--contact", default="")
    ap.add_argument("--products", default="Synthetic Urine; Synthetic CSF")
    ap.add_argument("--proof", default="ISO 13485 certified")
    ap.add_argument("--cta", default="15-minute call")
    ap.add_argument("--from_name", default="Maykel")
    ap.add_argument("--from_company", default="TruSample")
    ap.add_argument("--from_email", default="info@trusample.bio")
    args = ap.parse_args()

    hi = f"Hi {args.contact}," if args.contact else "Hi," 

    subject = f"Partnership: {args.from_company} synthetic reference materials ({args.proof})"

    email = f"""{hi}

I’m {args.from_name} from {args.from_company}. We manufacture consistent synthetic reference materials (e.g., {args.products}) designed for assay validation, proficiency testing, and method development.

What makes us a strong fit for distribution:
- {args.proof}
- Lot traceability + COA/spec options
- Custom formulations + packaging options for programs

If you’re open to it, I’d love to set up a quick {args.cta} to learn what product categories your customers request most and share our current lineup + pricing structure.

Best,
{args.from_name}
{args.from_company}
{args.from_email}
"""

    linkedin = f"""{hi} I’m {args.from_name} at {args.from_company}. We produce {args.proof} synthetic reference materials (e.g., {args.products}) for validation/PT workflows. Open to a quick {args.cta} to explore distributor fit?"""

    xdm = f"""Hi — {args.from_name} from {args.from_company}. We make {args.proof} synthetic matrices ({args.products}) for assay validation/PT. Open to a quick {args.cta} to discuss distribution?"""

    notes = dedent("""
    PERSONALIZATION IDEAS
    - Mention one category they already sell (IVD controls, reagents, QC materials).
    - Mention ship regions (US/EU/LatAm) if you know.
    - If they focus on academia vs clinical, adjust use-cases accordingly.
    """).strip()

    print("SUBJECT:\n" + subject)
    print("\nEMAIL:\n" + email.strip())
    print("\nLINKEDIN DM:\n" + linkedin.strip())
    print("\nX DM:\n" + xdm.strip())
    print("\n" + notes)


if __name__ == "__main__":
    main()
