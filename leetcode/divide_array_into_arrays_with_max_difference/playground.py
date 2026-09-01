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
from helpers import assert_divide_array, run_divide_array
from solution import Solution

# %%
# Example test case
nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k = 2
expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]

# %%
result = run_divide_array(Solution, nums, k)
result

# %%
assert_divide_array(result, expected, k)
