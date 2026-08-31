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
from helpers import assert_longest_ones, run_longest_ones
from solution import Solution

# %%
# Example test case
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
expected = 6

# %%
result = run_longest_ones(Solution, nums, k)
result

# %%
assert_longest_ones(result, expected)
