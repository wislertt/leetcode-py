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
from helpers import assert_contains_nearby_duplicate, run_contains_nearby_duplicate
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 1]
k = 3
expected = True

# %%
result = run_contains_nearby_duplicate(Solution, nums, k)
result

# %%
assert_contains_nearby_duplicate(result, expected)
