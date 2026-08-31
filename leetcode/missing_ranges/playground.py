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
from helpers import assert_find_missing_ranges, run_find_missing_ranges
from solution import Solution

# %%
# Example test case
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
expected = [[2, 2], [4, 49], [51, 74], [76, 99]]

# %%
result = run_find_missing_ranges(Solution, nums, lower, upper)
result

# %%
assert_find_missing_ranges(result, expected)
