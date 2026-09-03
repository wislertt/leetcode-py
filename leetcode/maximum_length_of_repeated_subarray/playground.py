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
from helpers import assert_find_length, run_find_length
from solution import Solution

# %%
# Example test case
nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
expected = 3

# %%
result = run_find_length(Solution, nums1, nums2)
result

# %%
assert_find_length(result, expected)
