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
from helpers import assert_count_range_sum, run_count_range_sum
from solution import Solution

# %%
# Example test case
nums: list[int] = [-2, 5, -1]
lower = -2
upper = 2
expected = 3

# %%
result = run_count_range_sum(Solution, nums, lower, upper)
result

# %%
assert_count_range_sum(result, expected)
