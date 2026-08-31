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
from helpers import assert_shortest_subarray, run_shortest_subarray
from solution import Solution

# %%
# Example test case
nums = [2, -1, 2]
k = 3
expected = 3

# %%
result = run_shortest_subarray(Solution, nums, k)
result

# %%
assert_shortest_subarray(result, expected)
