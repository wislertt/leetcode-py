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
from helpers import assert_can_divide_into_subsequences, run_can_divide_into_subsequences
from solution import Solution

# %%
# Example test case
nums = [1, 2, 2, 3, 3, 4, 4]
k = 3
expected = True

# %%
result = run_can_divide_into_subsequences(Solution, nums, k)
result

# %%
assert_can_divide_into_subsequences(result, expected)
