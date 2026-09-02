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
from helpers import assert_max_number, run_max_number
from solution import Solution

# %%
# Example test case
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
expected = [9, 8, 6, 5, 3]

# %%
result = run_max_number(Solution, nums1, nums2, k)
result

# %%
assert_max_number(result, expected)
