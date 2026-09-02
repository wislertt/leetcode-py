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
from helpers import assert_find_difference, run_find_difference
from solution import Solution

# %%
# Example test case
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
expected = [[1, 3], [4, 6]]

# %%
result = run_find_difference(Solution, nums1, nums2)
result

# %%
assert_find_difference(result, expected)
