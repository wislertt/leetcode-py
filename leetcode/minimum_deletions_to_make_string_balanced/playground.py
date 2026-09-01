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
from helpers import assert_minimum_deletions, run_minimum_deletions
from solution import Solution

# %%
# Example test case
s = "aababbab"
expected = 2

# %%
result = run_minimum_deletions(Solution, s)
result

# %%
assert_minimum_deletions(result, expected)
