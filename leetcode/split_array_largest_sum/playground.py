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
from helpers import assert_split_array, run_split_array
from solution import Solution

# %%
# Example test case
nums = [7, 2, 5, 10, 8]
k = 2
expected = 18

# %%
result = run_split_array(Solution, nums, k)
result

# %%
assert_split_array(result, expected)
