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
from helpers import assert_range_sum, run_range_sum
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 2, 3, 4]
n = 4
left = 1
right = 5
expected = 13

# %%
result = run_range_sum(Solution, nums, n, left, right)
result

# %%
assert_range_sum(result, expected)
