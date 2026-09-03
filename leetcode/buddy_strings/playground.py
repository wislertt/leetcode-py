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
from helpers import assert_buddy_strings, run_buddy_strings
from solution import Solution

# %%
# Example test case
s = "ab"
goal = "ba"
expected = True

# %%
result = run_buddy_strings(Solution, s, goal)
result

# %%
assert_buddy_strings(result, expected)
