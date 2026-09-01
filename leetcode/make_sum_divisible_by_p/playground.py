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
from helpers import assert_min_subarray, run_min_subarray
from solution import Solution

# %%
# Example test case
nums = [3, 1, 4, 2]
p = 6
expected = 1

# %%
result = run_min_subarray(Solution, nums, p)
result

# %%
assert_min_subarray(result, expected)
