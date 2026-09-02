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
from helpers import assert_find_unsorted_subarray, run_find_unsorted_subarray
from solution import Solution

# %%
# Example test case
nums = [2, 6, 4, 8, 10, 9, 15]
expected = 5

# %%
result = run_find_unsorted_subarray(Solution, nums)
result

# %%
assert_find_unsorted_subarray(result, expected)
