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
from helpers import assert_maximum_value_sum, run_maximum_value_sum
from solution import Solution

# %%
# Example test case
nums = [1, 2, 1]
k = 3
edges = [[0, 1], [0, 2]]
expected = 6

# %%
result = run_maximum_value_sum(Solution, nums, k, edges)
result

# %%
assert_maximum_value_sum(result, expected)
