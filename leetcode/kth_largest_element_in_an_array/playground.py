# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_find_kth_largest, run_find_kth_largest
from solution import Solution

# %%
# Example test case
nums = [3, 2, 1, 5, 6, 4]
k = 2
expected = 5

# %%
result = run_find_kth_largest(Solution, nums, k)
result

# %%
assert_find_kth_largest(result, expected)
