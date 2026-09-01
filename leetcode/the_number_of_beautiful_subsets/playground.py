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
from helpers import assert_beautiful_subsets, run_beautiful_subsets
from solution import Solution

# %%
# Example test case
nums: list[int] = [2, 4, 6]
k = 2
expected = 4

# %%
result = run_beautiful_subsets(Solution, nums, k)
result

# %%
assert_beautiful_subsets(result, expected)
