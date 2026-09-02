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
from helpers import assert_find_pairs, run_find_pairs
from solution import Solution

# %%
# Example test case
nums = [3, 1, 4, 1, 5]
k = 2
expected = 2

# %%
result = run_find_pairs(Solution, nums, k)
result

# %%
assert_find_pairs(result, expected)
