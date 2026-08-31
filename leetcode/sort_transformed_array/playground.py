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
from helpers import assert_sort_transformed_array, run_sort_transformed_array
from solution import Solution

# %%
# Example test case
nums: list[int] = [-4, -2, 2, 4]
a = 1
b = 3
c = 5
expected = [3, 9, 15, 33]

# %%
result = run_sort_transformed_array(Solution, nums, a, b, c)
result

# %%
assert_sort_transformed_array(result, expected)
