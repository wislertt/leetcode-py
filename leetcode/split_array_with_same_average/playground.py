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
from helpers import assert_split_array_same_average, run_split_array_same_average
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4, 5, 6, 7, 8]
expected = True

# %%
result = run_split_array_same_average(Solution, nums)
result

# %%
assert_split_array_same_average(result, expected)
