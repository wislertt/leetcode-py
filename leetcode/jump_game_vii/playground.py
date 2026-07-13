# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_can_reach, run_can_reach
from solution import Solution

# %%
# Example test case
s = "011010"
min_jump = 2
max_jump = 3
expected = True

# %%
result = run_can_reach(Solution, s, min_jump, max_jump)
result

# %%
assert_can_reach(result, expected)
