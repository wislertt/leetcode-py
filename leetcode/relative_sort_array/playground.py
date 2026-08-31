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
from helpers import assert_relative_sort_array, run_relative_sort_array
from solution import Solution

# %%
# Example test case
arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
expected = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]

# %%
result = run_relative_sort_array(Solution, arr1, arr2)
result

# %%
assert_relative_sort_array(result, expected)
