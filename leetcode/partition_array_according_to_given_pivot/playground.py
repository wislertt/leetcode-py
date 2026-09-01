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
from helpers import assert_pivot_array, run_pivot_array
from solution import Solution

# %%
# Example test case
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
expected = [9, 5, 3, 10, 10, 12, 14]

# %%
result = run_pivot_array(Solution, nums, pivot)
result

# %%
assert_pivot_array(result, expected)
