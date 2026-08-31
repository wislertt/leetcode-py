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
from helpers import assert_smallest_distance_pair, run_smallest_distance_pair
from solution import Solution

# %%
# Example test case
nums = [1, 3, 1]
k = 1
expected = 0

# %%
result = run_smallest_distance_pair(Solution, nums, k)
result

# %%
assert_smallest_distance_pair(result, expected)
