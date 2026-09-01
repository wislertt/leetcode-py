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
from helpers import assert_zero_filled_subarray, run_zero_filled_subarray
from solution import Solution

# %%
# Example test case
nums = [1, 3, 0, 0, 2, 0, 0, 4]
expected = 6

# %%
result = run_zero_filled_subarray(Solution, nums)
result

# %%
assert_zero_filled_subarray(result, expected)
