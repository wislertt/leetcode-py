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
from helpers import assert_max_increase_keeping_skyline, run_max_increase_keeping_skyline
from solution import Solution

# %%
# Example test case
grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
expected = 35

# %%
result = run_max_increase_keeping_skyline(Solution, grid)
result

# %%
assert_max_increase_keeping_skyline(result, expected)
