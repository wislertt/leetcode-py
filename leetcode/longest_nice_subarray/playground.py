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
from helpers import assert_longest_nice_subarray, run_longest_nice_subarray
from solution import Solution

# %%
# Example test case
nums = [1, 3, 8, 48, 10]
expected = 3

# %%
result = run_longest_nice_subarray(Solution, nums)
result

# %%
assert_longest_nice_subarray(result, expected)
