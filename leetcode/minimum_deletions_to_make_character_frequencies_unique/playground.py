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
from helpers import assert_min_deletions, run_min_deletions
from solution import Solution

# %%
# Example test case
s = "aaabbbcc"
expected = 2

# %%
result = run_min_deletions(Solution, s)
result

# %%
assert_min_deletions(result, expected)
