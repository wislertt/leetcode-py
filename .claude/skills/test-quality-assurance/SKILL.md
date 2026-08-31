---
name: test-quality-assurance
description: Test quality assurance workflow for LeetCode problems - verifies reproducibility, fixes linting issues, and ensures test structure matches JSON templates. Use ONLY when user explicitly requests test quality assurance via /test-quality-assurance command.
---

# Test Quality Assurance Rules

## CRITICAL: Follow These Steps EXACTLY - No Deviations

### 1. Problem Resolution

- Use active file context or user-provided problem name
- If unclear, run: `uv run python -m leetcode_py.tools.check_test_cases --threshold=10 --max=1`

### 2. Test Reproducibility Verification Process

**MANDATORY 6-Step Process - Execute in Order:**

```bash
# Step 1: Backup original files
cp -r leetcode/{problem_name} leetcode/{problem_name}_backup

# Step 2: Regenerate from JSON template (use bake, NOT uv run)
bake p-gen -p {problem_name} -f

# Step 3: Restore original solution ONLY
cp leetcode/{problem_name}_backup/solution.py leetcode/{problem_name}/solution.py

# Step 4: Verify linting pass (CRITICAL for CI)
bake lint

# Step 5: Verify tests pass (expected to fail if solution is incomplete)
bake p-test -p {problem_name}
# NOTE: in the batch-problem-creation flow the solution is implemented BEFORE this
# step, so tests MUST pass here. A failure = real defect: wrong expected values in
# the JSON test_cases (most common — see problem-creation.md tree gotchas) or a
# wrong solution. Debug it; do not dismiss it as "incomplete solution".

# Step 6: Cleanup
rm -rf leetcode/{problem_name}_backup
```

### 3. What NOT to Do

- **NEVER edit cookiecutter templates** (`{{cookiecutter.problem_name}}/` files)
- **NEVER use `uv run python -m leetcode_py.cli.main gen`** - use `bake p-gen` instead
- **NEVER modify helpers.py manually** - let regeneration handle it
- **NEVER skip ty verification** - this is the main CI issue
- **NEVER assume tests will pass** - they may fail if solution is incomplete
- **NEVER use `null` in JSON templates** - use `None` for Python None values

### 4. What to Do

- **ALWAYS use `bake p-gen -p {problem_name} -f`** for regeneration
- **ALWAYS verify ty passes** before considering task complete
- **ALWAYS restore original solution** after regeneration
- **ALWAYS check JSON template** if ty fails (look for `assert_assert_` bugs)
- **ALWAYS use `None` not `null` in JSON templates** for Python None values

## Test Case Standards

### Coverage Requirements

- **Minimum 12 test cases** per problem
- **Edge cases**: Empty inputs, single elements, boundary values
- **Corner cases**: Maximum/minimum constraints, duplicates, sorted arrays
- **Normal cases**: Mixed scenarios with varied complexity

### JSON Format

- **CRITICAL**: Use `None` NOT `null` for Python None values in test cases
    - JSON templates use `None` directly: `"[1, None, 2]"` NOT `"[1, null, 2]"`
    - This ensures generated Python code passes linting (ruff/ty check for undefined name `null`)
- Use single quotes for Python strings: `'hello'` not `"hello"`
- Follow existing parametrize format
- Ensure valid Python list syntax in test_cases field

## Quick Commands

### CLI Commands (Recommended)

```bash
# Generate enhanced problem
uv run lcpy gen -s {problem_name} -o leetcode --force

# Test specific problem
bake p-test -p {problem_name}

# Lint check
bake lint
```

### Development Commands

```bash
# Find problems needing enhancement
uv run python -m leetcode_py.tools.check_test_cases --threshold=10

# Check all problems (no limit)
uv run python -m leetcode_py.tools.check_test_cases --threshold=10 --max=none

# Check with custom threshold
uv run python -m leetcode_py.tools.check_test_cases --threshold=12

# Generate from JSON template (uses uv run lcpy internally)
bake p-gen -p {problem_name} -f
```

## Common Issues & Solutions

### Issue: \`assert_assert_missing_number\` Error

**Cause**: JSON template has \`helpers*assert_name: "assert_missing_number"\` but template adds \`assert*\` prefix
**Solution**: Change JSON to \`helpers_assert_name: "missing_number"\` so template generates \`assert_missing_number\`

### Issue: ty Import Errors

**Cause**: Regenerated helpers.py doesn't match test imports
**Solution**: Use \`bake p-gen\` (not uv run) and verify JSON template is correct

### Issue: Tests Fail After Regeneration

**Expected**: Tests may fail if solution is incomplete (returns 0 or placeholder)
**Action**: This is normal - focus on ty passing, not test results
**Exception**: if the solution is already implemented (batch flow), failures are real
defects — fix the JSON test cases or the solution, then re-run the 6 steps

### Issue: pre-commit flags solution.py (B905 / E741 / RUF012 / N806 / ty list invariance)

**Cause**: `bake lint` during QA runs a narrower ruff config than the pre-commit hook, so `zip()` without `strict=` (B905), variable names like `l` (E741), mutable class-attribute defaults (RUF012), uppercase locals like `MOD` (N806), and list-invariance type mismatches in ty pass QA and surface only at batch finalization.

- Fix: `zip(s, t)` → `zip(s, t, strict=True)`; rename `l`/`I`/`O` variables (`left_val`, etc.); class-level constant lists → tuples (`BELOW_20: tuple[str, ...] = (...)`) or annotate with `typing.ClassVar`; `MOD = 1_000_000_007` → lowercase `mod` (N806, recurs on every modulo problem); annotate accumulators with the full return element type (`result: list[TreeNode[int] | None]`, not `list[TreeNode[int]]` returned against `-> list[TreeNode[int] | None]` — ty rejects the narrowing under list invariance); a `float('-inf')` sentinel in an int-returning DP poisons derived values into `float` (ty `invalid-return-type`) — prefer a type-pure int sentinel like `-1` for non-negative domains (hit with 741 Cherry Pickup); a nested `dfs(node: TreeNode[int] | None, ...)` whose body touches `node.val`/`node.left`/`node.right` passes `bake lint` but fails pre-commit ty with one `unresolved-attribute` per access — ty does not narrow through the call site when `root` is `Optional`, so add `if node is None: return` at the top of the DFS (hit with 988, 7 errors at once). Generated helpers add three more: RUF005 list concatenation in return expressions → unpack instead (`[node.val, *left, *right]`, hit with 889); E731 lambda assigned to a name → rewrite as a `def` with return type (hit with 894); ty `unresolved-attribute` when calling `.to_list()` on a `TreeNode | None` element — `assert all(x is not None ...)` does NOT narrow a comprehension variable; filter into a new list (`roots = [t for t in result if t is not None]`) and assert equal length (hit with 894). All are fixed at the JSON level (`helpers_assert_body` / `helpers_content`) or in `solution.py`, never in other generated files
- Hit with 273 Integer to English Words: lookup-table lists (`BELOW_20 = [...]`) at class level flagged `RUF012 Mutable default value for class attribute`
- Hit with 552/576/629 (`MOD` → N806) and 652 (ty `invalid-return-type` on list invariance)
- E501 also fires on COMMENTS: a complexity comment listing per-method costs (`# Time: get O(index), add_at_index O(index), ...`) overflows col 100 — compress or split it (hit with 707 Design Linked List)
- Prevention: write solutions ruff-clean from the start (see problem-creation.md, Batch Flow Notes section)

### Issue: \`null\` vs \`None\` in JSON Templates

**Cause**: JSON template uses \`null\` which causes linting errors in generated Python code

- Error: \`F821 Undefined name 'null'\` from ruff/ty
- Generated test files contain \`null\` which is not valid Python

**Solution**: Update JSON template to use \`None\` instead of \`null\`

- Change: \`"([1, null, 2], 3, 1)"\` → \`"([1, None, 2], 3, 1)"\`
- This applies to \`test_cases\` list and \`playground_setup\` fields
- After fixing JSON, regenerate with \`bake p-gen -p {problem_name} -f\`
- Generated code will now pass linting without manual edits

### Issue: hand-invented inputs pass value-range checks but violate STRUCTURAL constraints

**Cause**: verifying each entry against value ranges (\`grid[i][j]\` is 0 or 1, \`nums[i] <= 10^4\`) is not enough — shape invariants stated in the constraints must be checked too. Hit with 827 Making A Large Island: the statement guarantees an \`n x n\` (square) grid, but a test case like \`[[1], [1]]\` is 2x1; it passes all value checks and then crashes matrix-indexing solutions with \`IndexError\`, which reads as a solution bug rather than a test-data bug

- **Fix**: include shape invariants (\`grid.length == grid[i].length\`, row/col counts, ordering guarantees like "graph[i] is strictly increasing") in the reference-implementation verification script — assert the STRUCTURE of every input, not just element values
- Drop or reshape any case that violates a structural constraint, even if the expected output "looks right"

## Success Criteria

- **ty passes** with no errors (CRITICAL for CI)
- **Test structure matches JSON template** exactly
- **Original solution preserved** (user's code intact)
- **helpers.py generated correctly** (no \`assert*assert*\` bugs)
- **Reproducibility verified** (can regenerate consistently)

## When to Use This Workflow

- GitHub Actions CI failures due to ty errors
- Test reproducibility verification requests
- Need to ensure test structure matches JSON template
- CI test failures in reproducibility checks
