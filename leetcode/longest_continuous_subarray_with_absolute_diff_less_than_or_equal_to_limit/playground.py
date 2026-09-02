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
from helpers import assert_longest_subarray, run_longest_subarray
from solution import Solution

# %%
# Example test case
nums = [8, 2, 4, 7]
limit = 4
expected = 2

# %%
result = run_longest_subarray(Solution, nums, limit)
result

# %%
assert_longest_subarray(result, expected)
