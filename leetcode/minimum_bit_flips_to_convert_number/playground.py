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
from helpers import assert_min_bit_flips, run_min_bit_flips
from solution import Solution

# %%
# Example test case
start = 10
goal = 7
expected = 3

# %%
result = run_min_bit_flips(Solution, start, goal)
result

# %%
assert_min_bit_flips(result, expected)
