---
name: kimi
description: Integration with Kimi Moderato (Moonshot AI) API for CRM, email, and website automation. Use when needing to call Kimi AI endpoints for leads, campaigns, and page updates.
---

# Kimi API Integration

## When to use this skill
Use when you need to call Kimi AI's Moonshot Open Platform REST API to automate CRM, email campaigns, or website tasks directly from Clawdbot.

## Prerequisites
1. Obtain your Moonshot AI API key and set it in the environment:

   ```bash
   export MOONSHOT_API_KEY="YOUR_MOONSHOT_API_KEY"
   ```

2. Ensure `curl` and `jq` are installed on the system (for HTTP calls and JSON parsing).

## Making a Chat Completion Request
Use `curl` to send a request to the Kimi API. Example:

```bash
curl -s https://api.moonshot.ai/v1/chat/completions \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "k2.5",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant for managing CRM and email campaigns."},
      {"role": "user", "content": "<<YOUR_PROMPT_HERE>>"}
    ]
  }' | jq .
```

- Replace `model` with the desired Kimi model (e.g., `k2`, `k1.5`, or `k2.5`).
- Update the `system` message to suit your workflow.

## Example: Create a New CRM Lead
```bash
curl -s https://api.moonshot.ai/v1/chat/completions \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "k2.5",
    "messages": [
      {"role": "system", "content": "You are a CRM assistant that creates leads."},
      {"role": "user", "content": "Create a new lead: Company=Acme Inc., Contact=Alice, Email=alice@acme.com"}
    ]
  }' | jq .
```

## References
- API reference details: see [`references/api_docs.md`](references/api_docs.md)
