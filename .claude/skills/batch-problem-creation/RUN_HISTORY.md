# Batch Run History + Experiment Registry

Git-tracked record for the batch-problem-creation flow. Lives beside the skill it measures so history is versioned with skill changes.

## Experiments

Format: `- {ID} {title} | {status: proposed/testing/validated/rejected} | proposed {date} | hypothesis | success criteria | metric to watch`

- E1 parallel subagent spawn (3 concurrent) | validated | 2026-09-01 | Removing the agent-side tags.json5 insert (main inserts at gate 2.0 from agent-reported dir names) eliminates the only shared-file write, so 3 agents can run concurrently; wall time drops ~3x | (a) zero tag-race/corruption failures at gates 2.0-2.2, (b) wall time per problem < 75s (sequential baseline ~150s), (c) no boundary violations from concurrency confusion | wall seconds per problem; gate results. VALIDATED 2026-09-01 batch 9: gates clean, ~68s wall/problem (2035s agent time / 3 lanes), 0 violations
- E2 p-gen tag-absence tolerance | validated | 2026-09-01 | `bake p-gen` succeeds on a JSON absent from tags.json5 (prerequisite for E1) | scratch-problem p-gen run with no tags entry passes clean | one-shot check, PASSED 2026-09-01 (zzz_scratch_tag_test)

## Run history

Format: `{date} batch {n}: {count} problems, {mode}, {wall/agent time}, FAILs {n}, gates {pass/fail}, violations {n}, notes`

- 2026-09-01 batch 8: 101 problems (queue 1376-1846), sequential 1-at-a-time, agent durations ~65-630s each (~150s avg, ~4.2h total), FAILs 0, gates all PASS, boundary violations 1 (agent ran bake check-consistency off-script; fixed wording mid-batch), notes: first subagent-flow run; main context stayed near-flat (~500 tokens/problem); 3 false-FAILs at re-test from slug/dir-name mismatch (fixed); 15 premium problems diverted to unscrapable queue
- 2026-09-01 batch 9: 10 problems (unscrapable queue 1133-1168, full unscrapable web flow), parallel 3-concurrent (E1 validated), agent durations 134-328s each (~203s avg, ~34 min total, ~68s/problem wall), FAILs 0, gates all PASS (pre-commit clean, tag sync clean, consistency PASSED), violations 0, notes: 2 queue slugs misnamed (1135 real = Connecting Cities With Minimum Cost, 1168 real = Optimize Water Distribution; existing gotcha caught both); 2 SQL problems (1141/1142) were picked by the waterfall despite the non-Python screen, moved to NON_PYTHON_PROBLEMS; --take replacement pulls re-issued already-picked unscrapable entries (queue state) so replacements were taken from queue order manually
