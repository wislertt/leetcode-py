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
from helpers import assert_contains_nearby_almost_duplicate, run_contains_nearby_almost_duplicate
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 1]
index_diff = 3
value_diff = 0
expected = True

# %%
result = run_contains_nearby_almost_duplicate(Solution, nums, index_diff, value_diff)
result

# %%
assert_contains_nearby_almost_duplicate(result, expected)
