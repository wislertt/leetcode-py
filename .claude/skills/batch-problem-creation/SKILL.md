---
name: batch-problem-creation
argument-hint: "[count]"
description: Batch creation workflow for multiple LeetCode problems - loops through problem creation, solution implementation, and quality assurance for a specified count. Accepts optional count argument (e.g., /batch-problem-creation 10) or the keyword "unscrapable" to drain the not-yet-done queue in unscrapable.py via web-sourced data (/batch-problem-creation unscrapable). Defaults to 5 if no argument. Use ONLY when user explicitly requests batch creation via /batch-problem-creation command.
---

# Batch Problem Creation Command

## Assistant Workflow

1. **Parse arguments**: If `$ARGUMENTS` contains the keyword `unscrapable`, run the **Creating Unscrapable Problems from the Web** flow (bottom of this file) instead of the normal loop. Otherwise use `$ARGUMENTS` as count (valid integer); default 5 if absent
2. **Pre-assign problems** (main context): find N problems in one pass, scrape each to a /tmp file WITHOUT reading its content (Step 1.1)
3. **Per-problem subagent loop**: spawn one `general-purpose` subagent per problem; the agent does JSON creation, tag insert, p-gen, solution, QA. Main context only sees the agent's short report (Step 1.2-1.4)
4. **Finalize the whole batch** (main context): pre-commit, tag sync check, consistency check (in order — see Batch Finalization)
5. **Summarize**: batch results + skill improvement suggestions

**Why subagents**: a problem costs 30-60k context tokens when done inline (scrape dumps, JSON scripts, p-gen/test output). A subagent does the same work in its own context; the orchestrator pays only ~200-500 tokens per problem (spawn prompt + report). This keeps main context near-flat for any batch size.

## Step 1: Problem Creation Loop

### 1.1: Pre-Assign All Problems (main context, ONE pass)

**GOTCHA — never hand-copy the number into the scrape.** Transcribing `#214` as `257` scrapes the wrong problem silently and wastes a full cycle. Chain everything off script output.

**`next_problem.py --take N` is a waterfall**: it returns N distinct problems, one per line (`NUMBER TAG NAME SOURCE`), virtually consuming each pick so nothing repeats. Source priority: (1) `unscrapable` — the `UNSCRAPABLE_QUEUE` todo list in unscrapable.py, drained FIRST to keep the queue short; (2) `list` — registered problem lists via the best-list rule; (3) `new` — lowest LeetCode number absent from the database entirely (`TAG` is `none`, name unknown until scraped). Non-Python (SQL/shell) numbers are never picked. No-argument mode stays single-pick list-only.

**Route each manifest line by SOURCE**:

| SOURCE                                                | Handling                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list`                                                | `lcpy scrape` → normal flow (template as written)                                                                                                                                                                                                                                                                                 |
| `new`                                                 | `lcpy scrape` → normal flow, but `_tags: { "list": [] }` (NO tag — the problem belongs to no list) and gate 2.0 skips its tag insert                                                                                                                                                                                              |
| `unscrapable`                                         | NO `lcpy scrape` — premium/limited problems: fetch via the doocs/curl web flow (Unscrapable Problems Management, step 3), agent builds JSON from that data with the queue's tag (or `_tags: { "list": [] }` if tag is `none`). After creation, move the tuple from `UNSCRAPABLE_QUEUE` to `UNSCRAPABLE_HANDLED` in unscrapable.py |
| anything scraping as non-Python (SQL/shell statement) | do NOT create — append `(N, "kebab-name")` to `NON_PYTHON_PROBLEMS` in unscrapable.py, pull a replacement (see the replacement-pull gotcha below; for unscrapable batches take the next unclaimed queue line, not `--take`)                                                                                                       |

Run the lookups + scrapes in ONE bash call. Scrape output goes to files — NEVER print it to main context (it is the single largest context cost; the agent reads the file instead). Print only number, tag, slug, title:

```bash
uv run python .claude/.dev/next_problem.py --take {count} | while read -r line; do
  N=${line%% *}          # first token
  SOURCE=${line##* }     # LAST token — never `read -r N TAG NAME SOURCE`: zsh does NOT
  case "$SOURCE" in      # join the remainder into the last var, so a multi-word NAME
    unscrapable)         # ("(unknown until scraped)") silently mangles SOURCE and every
      echo "QUEUE $N none $NAME unscrapable_web_flow"   # no scrape; agent fetches via doocs/curl
      continue ;;
    new|list) ;;
    *) continue ;;       # malformed line — skip rather than scrape garbage
  esac
  uv run lcpy scrape -n "$N" > "/tmp/batch_scrape_${N}.json" 2>&1 < /dev/null
  rc=$?
  if [ $rc -ne 0 ] || head -c 1 "/tmp/batch_scrape_${N}.json" | grep -qv '{'; then
    echo "QUEUE $N none SCRAPE_FAILED $SOURCE"
  else
    META=$(python3 -c "import json; d=json.load(open('/tmp/batch_scrape_${N}.json')); print(d['slug'], '|', d['title'])")
    echo "QUEUE $N none $META $SOURCE"
  fi
done
```

**GOTCHA — zsh `read` word-splitting.** This machine's shell is zsh, and `read -r N TAG NAME SOURCE` does not join the line remainder into the last variable: `NAME` `(unknown until scraped)` leaves `SOURCE="until scraped) new"`, so a `[ "$SOURCE" = "new" ]` check silently skips EVERY line and the loop no-ops with zero output (2026-09-02 batch 17: 3 no-op scrape loops before root cause). Always key off the FIRST token (`${line%% *}`) and LAST token (`${line##* }`) only. If loop-based parsing misbehaves again, fall back to a small python script that reads the raw lines and parses the scrape JSONs (batch 15 precedent — worked first try).

Notes:

- A failed scrape (premium signature `Error fetching problem: 'NoneType' object is not iterable`, SQL `Error: Problem number N not found`) does NOT consume the number — handle per Error Handling below (premium → append to the unscrapable queue), then pull a replacement with another `--take` and scrape it
- **GOTCHA — replacement pulls must exclude every number already in the batch manifest, regardless of source.** Pick consumption is per-process (state is rebuilt from files each invocation), so a replacement `--take` called mid-batch re-issues already-picked picks — and any failures you just queued (hit 2026-09-01 batch 9: `--take 2` returned already-picked 1133-1152; batch 13, a pure `list` batch: `--take 2` returned the just-queued 1966/2021 and `--take 4` returned already-picked 1964/1968). One-pass recipe: `--take` WIDE in a single process (wide enough to cover queue entries + manifest), filter to the wanted SOURCE, drop manifest numbers, scrape the first survivors. For unscrapable batches an alternative is taking the next unclaimed `UNSCRAPABLE_QUEUE` lines directly
- **GOTCHA — the `unscrapable` source can hand you SQL problems.** The non-Python screen (`num not in non_python` in next_problem.py) reads `NON_PYTHON_PROBLEMS`, so it only catches entries ALREADY filed there — a still-queued SQL tuple (1141/1142 in batch 9) flows straight into the manifest. Verify each queue entry's language BEFORE the manifest (doocs folder title / README grep for SQL); if SQL, move the tuple to `NON_PYTHON_PROBLEMS` and take the next unclaimed queue line. Known SQL already filed: none left queued — new SQL discoveries still surface here
- The `QUEUE ...` lines are the batch manifest. Keep them; each line becomes one subagent spawn. Subagent prompts for `unscrapable` lines get the doocs-URL instructions instead of `{SCRAPE_PATH}` (see Unscrapable Problems Management step 3 for the URL pattern); prompts for `new` lines say tag is `none`

### 1.2: Spawn One Subagent Per Problem (sequential)

For each manifest line, spawn ONE agent with `subagent_type: "general-purpose"` (fresh empty context — NEVER `fork`, it inherits the orchestrator's whole conversation and defeats the purpose).

**Parallel mode (default 8 concurrent unless the user specifies a number; experiment E4)**: agents do NOT write `tags.json5` — the tag insert moved to finalization gate 2.0 (main-side, from the agent-reported dir names). That removes the only shared-file write, so agents own disjoint files and can run concurrently (p-gen writes only its own problem dir + scoped format/check on new dirs — verified in gen.py). `bake p-gen` tolerates a JSON absent from tags.json5 — verified 2026-09-01. **Hold the flight level by reconciling to target, not one-for-one**: on EVERY turn (each report, each spawn, each user message), count running agents (ListAgents) and spawn `target - running` replacements at once from the manifest. One-for-one refilling lags by 1-3 min per report and lets the flight sag to 3-4 (measured, E3 batch 13) — deficit spawning is what holds it at target. Brief overshoot is fine when several notifications land in one batch. Expect SHORT transient dips even with reconcile (notification latency + silently dropped notifications are real; 3/50 dropped in batch 13) — a sag of 1-2 for one turn is normal, a sag to half target that persists means dropped notifications: run the Step 1.3 fallback check. Ceiling note: ruff/ty/p-test are CPU-bound per agent, so past ~core-count concurrency each slows without wall-time gain — if agent durations inflate without FAILs or races, the cap is CPU, not the flow (E3 measured: durations did NOT inflate at 6 on the batch-13 machine).

**GOTCHA — never derive a spawn number from memory.** Every spawn prompt must be filled from a MANIFEST LINE read in that same turn (`awk '{print $2}' /tmp/batch_manifest.txt` to list unspawned numbers). Numbering refills from recall invents problems: 2026-09-02 batch 17 spawned 6 numbers (587-597) that were not in the manifest — 2 landed on SQL (dead spawns), 4 created unplanned problems, and a real manifest line (575) was skipped until the end-of-batch reconciliation caught it. Second consecutive batch with a manifest-discipline failure (batch 16 silently dropped 3 lines). Same rule as the scrape gotcha above, one level up: hand-transcription of numbers is where batches go wrong, whether into a scrape command or a spawn prompt. When refilling, take the LOWEST unspawned manifest number(s) not yet reported — and keep a spawned/set marker (e.g. touch `/tmp/batch_spawned_{N}`) if multiple reports land in one turn, so the same line is never double-spawned or skipped.

**Subagent prompt template** — fill `{N}`, `{TAG}`, `{SCRAPE_PATH}` (`/tmp/batch_scrape_{N}.json`) from the manifest line, verbatim otherwise:

```text
Create LeetCode problem #{N} in this repo. Work autonomously; report back concisely.

FIRST: read these two files completely before any other action:
- .claude/skills/problem-creation/SKILL.md
- .claude/skills/test-quality-assurance/SKILL.md
Follow them exactly — every gotcha in them is there because it cost a real cycle.

Input data: the problem is already scraped to {SCRAPE_PATH}. Do NOT re-scrape.
Read that file (it has description, examples, constraints, topics, python_code signature, image URLs).
The JSON's _tags should be { "list": ["{TAG}"] } — but do NOT run insert_tag.py; the orchestrator
inserts all tags at finalization (other agents run concurrently and would race on tags.json5).

Do, in order:
1. Build the JSON template at src/leetcode_py/cli/resources/leetcode/json/problems/{problem_name}.json
   per problem-creation.md (images, _tags: { "list": ["{TAG}"] } — if {TAG} is `none` use
   "list": [] and skip all tagging, 12+ test cases, single-quote
   playground strings, None not null). Write it via a python script that machine-verifies every
   test-case expectation with a reference implementation and asserts BEFORE json.dump — never
   hand-transcribe expectations.
2. bake p-gen -p {problem_name}  (fix the JSON, never generated files, re-run until clean)
3. Implement ONE optimal solution in the single Solution class in solution.py (design problems:
   the custom class only), ruff/ty-clean up front per problem-creation.md Batch Flow Notes.
4. Run the QA chain from test-quality-assurance.md step 2 (backup -> p-gen -f -> restore
   solution -> p-test -> cleanup). Repo-wide `bake lint` is NOT yours — the orchestrator runs
   it at finalization; but scoped lint IS yours: `uv run ruff check leetcode/{problem_name}`,
   `uv run ruff format --check leetcode/{problem_name}`, `uv run ty check leetcode/{problem_name}`
   must all be clean before you report PASS. Tests MUST pass (solution is implemented); a
   failure means bad JSON expectations or a wrong solution — fix it, do not dismiss it.
   SPIN GUARD: if p-test exceeds ~1 min on your 12-20 tiny cases, kill it — that is an
   infinite loop in the solution/helper, not slowness (check `ps` for a ~100% CPU pytest);
   find the spinning case by running cases individually and fix the root cause. Never report
   PASS off a truncated or early-ended output file.
5. Write the actual directory name you created (one line) to /tmp/batch_name_{N}.txt, so the
   orchestrator can insert the tag and re-test by real dir names — do NOT assume the scrape
   slug (they can differ, e.g. shorter names chosen to satisfy E501).

Boundaries — you own ONLY this problem:
- Touch only: your JSON file, leetcode/{problem_name}/, /tmp scratch files (including
  /tmp/batch_name_{N}.txt)
- Do NOT: edit bakefile.py, tags.json5, other problems' files, problem_lists/*.py,
  unscrapable.py; run `bake lint`, `bake check-consistency`, pre-commit, or any repo-wide
  command; git commit
- This is a subagent task: skip the brainstorming/superpowers skill ceremony; the two skill
  files above are your complete instructions.

Report back EXACTLY this and nothing else:
- problem_name: <name>
- status: PASS | FAIL
- tests: <count> passed
- if FAIL: one paragraph — what failed, the error, what you tried
- any deviation from the skills you had to make and why
```

### 1.3: After Each Agent Report (main context)

- PASS: `sed -i '' 's/    problem: str = ".*"/    problem: str = "{problem_name}"/' bakefile.py` — keeps `bake p-test` default pointing at the newest problem. Then reconcile the flight to target (count running, spawn the deficit from the manifest). The agent also wrote its real dir name to /tmp/batch_name_{N}.txt — authoritative for tag insert (gate 2.0) and Step 3 re-testing; do NOT derive names from the scrape slug (they can differ)
- FAIL: log reason for the summary; decide retry once vs skip per Error Handling. Do not debug inline — a failed agent's context is gone; if retrying, spawn a fresh agent including the failure paragraph in the prompt
- **GOTCHA — completion notifications can be silently dropped** (3 of 50 in batch 13: the agent left the roster with no notification ever arriving). If an agent seems long-running but you suspect it finished, do NOT respawn (it would collide on the same files) — check `/tmp/batch_name_{N}.txt` existence + `leetcode/<dir>` presence, then confirm with a scoped pytest run on that dir before counting it done or scheduling a respawn
- Suppressed-output discipline (the whole point of this design): never print scrape JSON, full p-gen logs, or full test output to main context. `| tail -3` or grep a count. If deeper inspection is needed, it belongs in the NEXT agent's prompt, not this conversation

### 1.4: What Moved Where (vs inline flow)

- Agent-side (its context, not yours): scrape reading, JSON writing + verification, p-gen cycles, solution implementation, QA chain, all gotcha application
- Orchestrator-side (main context): manifest, spawns, bakefile sed, tag insert (gate 2.0), finalization gates, summary
- Unchanged skills: problem-creation.md and test-quality-assurance.md are read BY THE AGENT — do not summarize them into the prompt beyond the pointers above; the files are the source of truth

## Step 2: Batch Finalization (MANDATORY — after ALL problems)

Five gates in order. Do NOT skip any.

### 2.0: Tag Insert (main-side — agents no longer insert their own)

Agents run concurrently and don't touch tags.json5; insert all batch tags here. Keep the name files — the Step 3 re-test still reads them (deleting them here cost a full wasted re-test cycle in one batch: all 30 problems printed MISSING_NAMEFILE and the mapping had to be rebuilt by hand). Cleanup happens at the END of Step 3:

```bash
grep '^QUEUE' /tmp/batch_manifest.txt | while read -r _ N TAG _; do
  NAME=$(cat "/tmp/batch_name_${N}.txt")
  if [ "$TAG" != "none" ]; then
    uv run python .claude/.dev/insert_tag.py "$TAG" "$NAME"
  fi
done
```

- Before inserting, verify each name file exists (`ls /tmp/batch_name_*.txt | wc -l` equals problem count) — a missing file means that agent never reported; handle per Error Handling before proceeding
- **GOTCHA — validate name-file CONTENT before insert, not just existence.** An agent wrote its problem NUMBER (`1180`) instead of the dir name into its name file; `insert_tag.py` happily bisected the numeric string to a bogus position in tags.json5 and the downstream sed fix preserved that position, costing 2 extra cycles (name fix + position fix + pre-commit rerun). Guard: each name must match `^[a-z][a-z0-9_]*$` — on mismatch, look up the real dir in `leetcode/` (or re-ask the agent) before running insert_tag.py. A second variant (453): the agent wrote a plausible but ABBREVIATED dir name (`min_moves_...`) while the real dir was `minimum_moves_...` — regex-clean but nonexistent. So also verify the dir and JSON actually exist (the re-test sweep would otherwise false-FAIL on the wrong name):

```bash
grep '^QUEUE' /tmp/batch_manifest.txt | while read -r _ N TAG _; do
  NAME=$(cat "/tmp/batch_name_${N}.txt")
  echo "$NAME" | grep -qE '^[a-z][a-z0-9_]*$' || { echo "BAD NAME FILE for $N: '$NAME'"; exit 1; }
  [ -d "leetcode/$NAME" ] || echo "MISSING DIR for $N: $NAME"
  [ -f "src/leetcode_py/cli/resources/leetcode/json/problems/${NAME}.json" ] || echo "MISSING JSON for $N: $NAME"
done
```

- Gate 2.2 (tag sync) must come out clean afterwards; if a name file's dir differs from the scrape slug, the name file wins

### 2.1: Pre-Commit (converts notebooks to .py)

```bash
pre-commit run -a
```

- `nb-to-py` converts every `leetcode/**/playground.ipynb` to `playground.py` and deletes the `.ipynb`; `lint` runs the full pipeline (sort_tags, check_tag_problems, gen_catalog, lint)
- Fix failures and re-run until clean
- **Why first**: `bake check-consistency` diffs `playground.py`, not `playground.ipynb` — notebooks MUST be converted before the consistency check

### 2.2: Tag Sync Check

```bash
uv run python .claude/.dev/update_tags.py
```

- Expect `No changes found in any of the specified tags.` — that IS the pass state (tags were synced per-problem during creation). `Missing`/`Removed` lines only appear on a dirty run
- A clean run creates NO `.claude/.dev/update_tags.json` — the `rm` no-ops. Remove the temp file if it exists after a dirty run
- **Gate semantics**: the gate counts only **Missing** lines. Pre-existing `Removed` lines do NOT block it — surface them to the user instead of silently resolving them
- **Warning**: do not resolve `Removed` lines on curated lists (neetcode-150, neetcode-250, blind-75, etc.) without the user's call — the `_tags.list` membership check is circular for batch-created problems and following it once cemented bogus tuples into curated lists. Ground truth = source-list membership by problem number
- If any `Missing`/`Removed` lines appear: **read and follow @.claude/skills/update-tags.md**

### 2.3: Consistency Check

```bash
bake check-consistency
```

- Regenerates ALL problems from JSON into a temp dir, converts notebooks, lints, then diffs against the working tree (original `leetcode/` is restored afterwards — solutions preserved)
- Expect `✅ Consistency check PASSED: all files match JSON source of truth`
- On drift (`Drift: leetcode/<problem>/<file>`): **read and follow @.claude/skills/consistency-fix.md**
- Loop until PASSED. `bake p-gen -f` reporting success does NOT mean consistency passes — only this command passing is real

### 2.4: Test Case Count Check

```bash
bake check-test-cases
```

- Must exit 0 (no problems at or below the default threshold — same command CI runs in `test-reproducibility.yml`, so local defaults and CI stay in lockstep). Success Criteria says 12+ per problem, but no other gate counts cases — p-test passes with any count, consistency only diffs generated-vs-JSON (a 10-case JSON is self-consistent), and the count otherwise surfaces only in CI. Batch 189's CI failure (campus_bikes, the_maze_iii at exactly 10) was caught nowhere locally. Runs in seconds — cheap fifth gate. On failure: add machine-verified cases to the JSON template AND mirror them into the generated `test_solution.py` by hand (regenerating clobbers solutions — see the p-gen -f warning below)
- **GOTCHA — a FAILED run can leave `leetcode/` as regenerated stubs.** `Restoring original leetcode/...` runs at the END of the pipeline; if the run aborts at its lint stage (ruff/ty error mid-batch), the restore never executes and the working tree keeps freshly generated TODO-stub solutions for EVERY problem. After any consistency failure, verify before continuing: `grep -l "TODO: Implement" leetcode/*/solution.py` — any hit means solutions were wiped (rewritable from session context or a /tmp copy; take the copy BEFORE the first consistency run, not after a failure). Only the PASSED run restores reliably
- **GOTCHA — flat `cp` can silently truncate the safety snapshot.** `cp leetcode/*/solution.py /tmp/dir/` copied exactly 1 file in one run (glob expansion mangled, likely by the rtk hook) — a silently-empty snapshot defeats its purpose. Use a per-problem loop and verify the count:

```bash
mkdir -p /tmp/batch_solutions_$(date +%Y%m%d)
for d in leetcode/*/; do
  [ -f "$d/solution.py" ] && cp "$d/solution.py" "/tmp/batch_solutions_$(date +%Y%m%d)/$(basename "$d")_solution.py"
done
ls /tmp/batch_solutions_$(date +%Y%m%d) | wc -l   # must equal number of problems
```

- **Warning**: `bake p-gen -p {problem_name} -f` overwrites `solution.py` with the TODO stub — backup and restore around ANY regen:

```bash
cp leetcode/{problem_name}/solution.py /tmp/solution_backup.py
bake p-gen -p {problem_name} -f
cp /tmp/solution_backup.py leetcode/{problem_name}/solution.py
```

## Step 3: Batch Summary

Report: total created, success rate, failed problems with reasons, finalization results. Then re-test all batch problems with `bake p-test -p {name}` and report counts.

**GOTCHA — derive re-test names from the agent manifest, not the scrape slug.** The dir name the agent created can differ from the scrape's `slug` (shorter names chosen for E501: 1415 → `k_th_lexicographical_...`, 1524 → `number_of_subarrays_...`, 1662 → `array_strings_are_equal`). Deriving from the slug produced 3/100 false FAILs and a wasted re-verify cycle. Agents write real dir names to `/tmp/batch_name_{N}.txt` (prompt step 5); test from those files. On a false-FAIL, check the dir exists under a different name before treating it as a real failure.

After the re-test loop completes, remove the name files (they are still needed until here — gate 2.0 deliberately does not delete them):

```bash
grep '^QUEUE' /tmp/batch_manifest.txt | while read -r _ N _; do rm -f "/tmp/batch_name_${N}.txt"; done
```

Finally, invoke the `commit-message` skill and show the user the ready-to-paste `git commit` command for the batch (do NOT execute it — the user stages and commits themselves).

### 3.1: Skill Improvement Suggestions (evidence-driven)

After the summary, review the run and **suggest** candidate updates to any skill used this session (batch-problem-creation, problem-creation, test-quality-assurance, update-tags, consistency-fix). Scope is the best overall skill, not just additions: new failure modes AND cuts — sections that wasted effort, duplicated another skill, or went stale. When in doubt, prefer deleting or merging over appending.

- **FIRST: read BOTH records**:
    - auto-memory `skill-suggestions-log` (machine-local, not in git) — a suggestion already recorded there is BLOCKED from re-proposal; if it was applied, re-suggesting means the skill text failed (say which wording); if it was skipped, the user chose not to act (do not resurrect)
    - `RUN_HISTORY.md` in this skill folder (git-tracked) — the experiment registry + per-batch run history
- **Evaluate open experiments against this run's metrics**: for each experiment in `testing` status in RUN_HISTORY.md, compare its success criteria against what this run actually recorded (wall time per problem, gate failures, boundary violations, context use). Move it to `validated` (then propose the skill change it implies) or `rejected` (record why, with numbers). An experiment needs at least one full batch of data before any verdict
- **Append this run's record** to RUN_HISTORY.md's run history: date, batch size, mode (sequential/parallel, concurrency), agent durations or wall time, FAIL count, gate results, boundary violations. One line per batch — this is the baseline future experiments are measured against. New process changes get registered in RUN_HISTORY.md too
- **Suggestion only. NEVER edit skill files** — the user decides and updates skills themselves (unless the user explicitly instructs the edit this session; then record the applied change in the log)
- **Bar for additions**: only what (a) will recur in future runs AND (b) existing skill content misses. Reject re-derivations (an existing gotcha catching the issue = skill working), refinements/widenings of working gotchas, niche one-offs (a greppable reference JSON suffices), run trivia. Test: name the exact step that failed AND the cycle it cost — no cost, no suggestion
- **Bar for cuts**: anything the run showed to be redundant, misleading, or unused — including steps followed out of habit that added no value
- **New process changes get proposed as experiments, not direct suggestions**: if a proposed change alters the run's shape (concurrency, flow order, gate structure), register it in RUN_HISTORY.md with a hypothesis, success criteria, and the metric to watch — the next run evaluates it. One-off gotcha fixes stay regular suggestions
- If nothing new was learned, say so explicitly — do not invent suggestions

## Error Handling

- **Continue the batch** when a problem fails — log the reason, move to the next, note it in the summary
- **NEVER edit generated files** (helpers.py, test_solution.py, README.md, ...) — fix the JSON template and regenerate. The ONLY exception is `solution.py`
- **Scrape failures**: premium → unscrapable queue; SQL → `NON_PYTHON_PROBLEMS`; transient API → retry once. For `new`-source failures the name is unknown until classified — fetch each failed number's title and file accordingly: `curl -s https://leetcode.ca/all/{N}.html | grep -o '<title>[^<]*'`; SQL/shell titles (Combine Two Tables, Word Frequency, ...) go to `NON_PYTHON_PROBLEMS`, premium Python titles to `UNSCRAPABLE_QUEUE` (batch 16: 21 numbers classified in one pass this way)

## Success Criteria

Each problem: all files generated, optimal solution implemented (single class), 12+ test cases, lint clean, `bake p-test` passes, QA chain run with solution preserved.

The batch: `pre-commit run -a` passes, tag sync clean, `bake check-consistency` PASSED, `bake check-test-cases` exits 0, all problems still pass `bake p-test` after finalization.

## Unscrapable Problems Management

### Queue placement

`unscrapable.py` has two lists: `UNSCRAPABLE_HANDLED` (already created or confirmed not applicable) and `UNSCRAPABLE_QUEUE` (the todo queue, discovery order). **Append new discoveries at the BOTTOM of `UNSCRAPABLE_QUEUE`** (appending at the top re-orders the queue against discovery order). Format: `(problem_number, "kebab-name")`. `next_problem.py` skips them automatically. Non-Python problems (SQL, shell) go to `NON_PYTHON_PROBLEMS` in the same file — never the queue.

### Premium clusters

Consecutive premium problems are common (e.g. 243-256). When two neighbors in a row fail, probe the whole range in a loop BEFORE adding exclusions one-by-one, then batch-add the failures:

```bash
for n in 247 248 249 250 251 252 253 254 255; do
  r=$(uv run lcpy scrape -n $n 2>&1 | head -c 30)
  case "$r" in Error*) echo "$n FAIL";; *) echo "$n OK";; esac
done
```

Sanity-check with a known-scrapable number first (e.g. `uv run lcpy scrape -n 205`) — every number failing means a broken network session, not a premium cluster.

### Creating Unscrapable Problems from the Web

When triggered via the `unscrapable` keyword, or any explicit request to work through `unscrapable.py` entries. Note: normal batches now drain the queue automatically (`--take` waterfall, source `unscrapable` — routing table in Step 1.1); this section covers the web-fetch details those agents need and the explicit keyword drain:

0. **Fetch ALL problem statements upfront, via `curl` — no Playwright needed.** `raw.githubusercontent.com` serves plain static text; `curl -s '<doocs-url>'` returns the full markdown faster than a browser and keeps the shared Playwright MCP free for other agents (Playwright cannot run parallel sessions). Do NOT use the `web_reader` MCP tool — user rule. Playwright is FALLBACK ONLY, for sources needing a real browser (or if curl is blocked) — when needed, request it as the flow's first tool call so the permission prompt lands before any file work. With either method: fetch every statement back to back at the start, then build the batch offline — no web dependency mid-loop
1. **Find not-yet-done entries**: `UNSCRAPABLE_QUEUE` is the todo queue; `UNSCRAPABLE_HANDLED` entries are done. Still verify against `leetcode/` dirs, `src/.../json/problems/`, and `tags.json5` — the split may be stale
2. **Determine tags from source lists**: grep the problem number in `.claude/.dev/problem_lists/*.py` (Python lists, not `.list` files). The matching list gives the tag — usually `neetcode` for the NeetCode All queue. Never stamp roadmap tags the number does not belong to. Verify membership with an unambiguous per-file check (`grep -c "($n," .claude/.dev/problem_lists/neetcode.py`) — a multi-file `grep -lE "\($n," .claude/.dev/problem_lists/*.py | sed ...` one-liner truncated the filename column in one batch and 7 in-neetcode problems were misread as unscrapable-only (`_tags: []`), surfacing only as 7 Missing lines at the tag-sync gate
3. **Fetch problem data** (see step 0 — fetch upfront via curl):
    - Primary: doocs/leetcode raw markdown mirror — carries the CURRENT official wording, examples, constraints, and topics (front matter `tags:`). URL pattern: `https://raw.githubusercontent.com/doocs/leetcode/main/solution/0100-0199/0156.Binary%20Tree%20Upside%20Down/README_EN.md` (century folder `0100-0199`, zero-padded number, URL-encoded title). `curl -s '<url>' | head -c 4000` — description + first solution. Title-guess 404? List the exact folder via GitHub API: `curl -s https://api.github.com/repos/doocs/leetcode/contents/solution/0200-0299 | grep '"name"'`
    - Fallback: `https://leetcode.ca/all/{N}.html` (older wording, usually no constraints) — curl first; Playwright only if it needs JS
    - **Playwright GOTCHA** (fallback only): `browser_evaluate` hangs on raw.githubusercontent pages (plain-text doc; eval stalls past 120s). Do NOT evaluate: navigate, then read the auto-saved snapshot at `.playwright-mcp/page-*.yml` — `head -c` the file
    - **Watch for revised statements**: doocs mirrors the current official text, which may differ from the classic version (163 Missing Ranges now returns `list[list[int]]` ranges and is Easy). Model the JSON on the fetched text, never on memory
    - **Cross-check the queue slug against the doocs folder name**: queue names are hand-entered and can be flat wrong (302 was queued as `smallest-range-covering-elements-from-k-arrays`; real 302 is Smallest Rectangle Enclosing Black Pixels — the K-Lists problem is 632, already in the repo). When the GitHub API listing or the fetched title disagrees with the queue tuple, the QUEUE is wrong: model the JSON on the real problem and correct the kebab-name when closing the loop in step 7
4. **Machine-verify every expectation** before writing the JSON (see problem-creation.md gotcha). Premium problems ship only 2-3 official examples, so most test cases are hand-invented — run a reference implementation over all of them (`uv run python` with `TreeNode[int].from_list` for tree round-trips)
    - **Design problems** (`solution_class_name` != `Solution`, e.g. 244 WordDistance): model on `design_hit_counter.json` — ops-sequence test cases (`['WordDistance', 'shortest', ...]` + per-op inputs), run helper instantiates the class mid-sequence
    - **Exponential-output problems** (result list grows 2^n, e.g. 247): use the `n_queens.json` dual-method pattern — method 1 asserts full SORTED lists for small n, method 2 asserts result COUNT only for large n (extra `assert_<name>_count` in `helpers_content`)
5. **Insert into tags.json5 carefully**: the `neetcode:` block begins with a metadata object (`{ tag: "neetcode-250", },`) before the string entries. Filter to quoted-string lines when bisecting; verify with `git diff` + `bake lint` (sort_tags), not a hand-rolled sort assert
6. Continue with the normal loop (p-gen, solution, QA, finalization)
7. **Close the loop in `unscrapable.py`**: once created and finalized, move the tuple from `UNSCRAPABLE_QUEUE` to `UNSCRAPABLE_HANDLED`. Only move what actually got created — non-Python problems go to `NON_PYTHON_PROBLEMS`, never the handled list. Entries found already-created during the step-1 staleness check also move at close time (verify they actually exist in `leetcode/`, the JSON dir, and tags before moving). If step 3 found the queue entry misnamed, fix the kebab-name in the moved tuple
