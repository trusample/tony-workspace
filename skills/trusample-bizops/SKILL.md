---
name: trusample-bizops
description: TruSample business-ops skills: generate enterprise-grade quote drafts, follow-up plans, distributor outreach, invoice/COA request templates, and repeatable workflows. Use when Maykel wants faster sales ops, email drafts, or standardized templates.
---

# TruSample BizOps

Use this skill to produce **drafts and workflows** for TruSample sales + operations. Default mode is **draft-only** (no sending). If the user explicitly asks to send, use the approved outbound channel/tool.

## What this skill covers
- Quote email drafts + clarifying questions
- Follow-up sequences (24h / 3d / 7d) with context
- Distributor outreach sequences
- COA / documentation request templates
- Invoice request templates / PO-ready language

## Quick usage
- Ask for the minimum inputs, but if the user wants "no questions", run with sane defaults and output a clear “assumptions” block.
- Prefer **B2B tone** (procurement-friendly, compliant).

## Scripts
- `scripts/quote_draft.py` — Generate quote email + questions + internal summary
- `scripts/followup_plan.py` — Follow-up schedule + message templates
- `scripts/outreach_draft.py` — Distributor outreach (email + LinkedIn + X DM)
- `scripts/invoice_request_draft.py` — Invoice/payment details email template
- `scripts/coa_request.py` — COA/spec request email template
- `scripts/product_spec_sheet.py` — One-page product/spec sheet (text)
- `scripts/meeting_brief.py` — Pre-call agenda + discovery + next steps
- `scripts/price_list_template.py` — Price list template (text or CSV)
- `scripts/quote_to_invoice_handoff.py` — Quote summary → invoice email + fulfillment checklist
- `scripts/objection_handling_snippets.py` — Reusable responses for common objections

Run scripts with `python3` and paste the output back to the user.

## Safety
- Do not send emails automatically. Provide drafts + ask for explicit “send it” instruction before using any outbound channel.
- Do not claim ISO scope/cert # unless provided.
