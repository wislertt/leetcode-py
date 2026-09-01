# Batch Run History + Experiment Registry

Git-tracked record for the batch-problem-creation flow. Lives beside the skill it measures so history is versioned with skill changes.

Keep this file short: full per-batch lines only for the last ~3 batches; older batches compressed to one aggregate line (keep only what a future experiment still needs as a baseline). Recurring failure modes and one-off gotchas belong in the skill-suggestions-log memory, not here.

## Experiments

Format: `- {ID} {title} | {status: proposed/testing/validated/rejected} | proposed {date} | hypothesis | success criteria | metric to watch`

No open experiments. Validated and closed:

- E1 parallel subagent spawn (3 concurrent) | validated + closed | 2026-09-01 | Removing the agent-side tags.json5 insert (main inserts at gate 2.0 from agent-reported dir names) eliminates the only shared-file write, so 3 agents can run concurrently; wall time drops ~3x | (a) zero tag-race failures, (b) wall/problem well under the ~150s sequential baseline, (c) no boundary violations | VALIDATED across batches 9-11: gates clean every run, ~68-103s wall/problem (3x vs sequential), 0 violations. Prerequisite E2 (`bake p-gen` tolerates a JSON absent from tags.json5) passed one-shot 2026-09-01.

## Run history

Format: `{date} batch {n}: {count} problems, {mode}, {wall/agent time}, FAILs {n}, gates {pass/fail}, violations {n}, notes`

- 2026-09-01 batches 3-8 (compressed): grew from inline flow to subagent flow at batch 8 (101 problems, queue 1376-1846, sequential 1-at-a-time, ~150s/problem, FAILs 0, 1 boundary violation fixed mid-batch). Lessons from these runs are already baked into the skill and the suggestions log — no baseline value left beyond the sequential ~150s/problem figure E1 was measured against.
- 2026-09-01 batch 9: 10 problems (unscrapable queue 1133-1168, full unscrapable web flow), parallel 3-concurrent (E1), agent durations 134-328s each (~203s avg, ~68s/problem wall), FAILs 0, gates all PASS, violations 0, notes: 2 queue slugs misnamed (1135, 1168; existing gotcha caught both); 2 SQL problems (1141/1142) picked by the waterfall despite the non-Python screen, moved to NON_PYTHON_PROBLEMS; --take replacement pulls re-issued already-picked unscrapable entries so replacements were taken from queue order manually
- 2026-09-01 batch 10: 10 problems (unscrapable queue 1180-1230, all fetched upfront via curl+GitHub API), parallel 3-concurrent (E1), agent durations 175-400s each (~269s avg, ~90s/problem wall), FAILs 0, gates PASS after 2 orchestrator-side fixes, violations 0, notes: 2 queue slugs misnamed (1215, 1230; existing gotcha caught both); one agent wrote its problem NUMBER instead of dir name into /tmp/batch_name_N.txt and insert_tag.py bisected the numeric string to a bogus tags.json5 position — 2 extra cycles; suggestions logged in skill-suggestions-log
- 2026-09-01 batch 11: 20 problems (unscrapable queue 1231-1533, all fetched upfront via curl+GitHub API), parallel 3-concurrent (E1), agent durations 127-645s each (~309s avg, ~103s/problem wall), FAILs 0, gates all PASS first try, violations 0, notes: 2 queue slugs misnamed (1258, 1259; existing gotcha caught both); 1533 statement contradicted the orchestrator's brief (no power-of-2 length, 400-call API limit) — agent modeled on fetched text, correct call; 3 agents (1272, 1474, 1533) each independently re-tested the E501 no-whitespace exemption — suggestion applied to problem-creation SKILL.md
- 2026-09-01 batch 12: 30 problems (first mixed batch: 8 unscrapable queue 1265-1836 + 2 premium scrape-fails re-routed to queue/web-flow 1868/1891 + 20 neetcode list 1849-1963), parallel 3-concurrent (E1), agent durations 97-435s each (~200s avg excl. outlier, ~67s/problem wall), FAILs 0, gates PASS after 1 orchestrator lint fix, violations 0, notes: 1265 solution shipped an infinite loop — spinning pytest at ~92% CPU burned ~34min before user flagged it; agent root-caused (non-terminating block-heads while loop + unbounded block print) and fixed same session, 14 pass in 0.37s after; 1849 SIM110 missed by agent's scoped ruff, caught at pre-commit (1 fix + rerun); 1942 renamed to `smallest_unoccupied_chair` for E501 (name file won, as designed); 1868/1891 appended to UNSCRAPABLE_QUEUE then moved to HANDLED same batch; 1279 created untagged (no list, correct); gate 2.0 deletes name files but Step 3 re-test needs them — orchestrator rebuilt mapping manually (suggestion logged)
