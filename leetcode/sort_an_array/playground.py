# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_sort_array, run_sort_array
from solution import Solution

# %%
# Example test case
nums = [5, 2, 3, 1]
expected = [1, 2, 3, 5]

# %%
result = run_sort_array(Solution, nums)
result

# %%
assert_sort_array(result, expected)
