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
from helpers import assert_largest_sum_of_averages, run_largest_sum_of_averages
from solution import Solution

# %%
# Example test case
nums = [9, 1, 2, 3, 9]
k = 3
expected = 20.0

# %%
result = run_largest_sum_of_averages(Solution, nums, k)
result

# %%
assert_largest_sum_of_averages(result, expected)
