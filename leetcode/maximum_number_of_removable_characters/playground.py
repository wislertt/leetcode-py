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
from helpers import assert_maximum_removals, run_maximum_removals
from solution import Solution

# %%
# Example test case
s = "abcacb"
p = "ab"
removable = [3, 1, 0]
expected = 2

# %%
result = run_maximum_removals(Solution, s, p, removable)
result

# %%
assert_maximum_removals(result, expected)
