# PLAYBOOK.md - Decision Frameworks

## When given a multi-step task
1. Write a script first, show the code, get confirmation
2. Run it, report actual output not assumed output
3. Update BRAIN.md with result
4. Move to next step

## When a tool or command fails
1. Diagnose the actual error message
2. Fix it directly - do not ask Maykel to fix it
3. If truly blocked, explain WHY with specifics, not vague "environment restrictions"

## Python - ALWAYS use venv /home/mhernandez/clawd/.venv/bin/python3

## Google API calls - ALWAYS use this auth pattern
See TOOLS.md

## Web search - ALWAYS use python3 ~/clawd/scripts/search.py "query"

## Before saying "I cannot do X"
1. Try at least 2 different approaches
2. Check TOOLS.md for existing solutions
3. Only then explain the blocker with specifics