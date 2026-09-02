# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_apply_substitutions, run_apply_substitutions
from solution import Solution

# %%
# Example test case
replacements = [["A", "abc"], ["B", "def"]]
text = "%A%_%B%"
expected = "abc_def"

# %%
result = run_apply_substitutions(Solution, replacements, text)
result

# %%
assert_apply_substitutions(result, expected)
