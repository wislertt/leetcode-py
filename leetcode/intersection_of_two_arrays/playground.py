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
from helpers import assert_intersection, run_intersection
from solution import Solution

# %%
# Example test case
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
expected = [4, 9]

# %%
result = run_intersection(Solution, nums1, nums2)
result

# %%
assert_intersection(result, expected)
