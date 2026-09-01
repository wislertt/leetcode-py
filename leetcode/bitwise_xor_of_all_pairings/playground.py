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
from helpers import assert_xor_all_nums, run_xor_all_nums
from solution import Solution

# %%
# Example test case
nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]
expected = 13

# %%
result = run_xor_all_nums(Solution, nums1, nums2)
result

# %%
assert_xor_all_nums(result, expected)
