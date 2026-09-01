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
from helpers import assert_kth_smallest_product, run_kth_smallest_product
from solution import Solution

# %%
# Example test case
nums1 = [2, 5]
nums2 = [3, 4]
k = 2
expected = 8

# %%
result = run_kth_smallest_product(Solution, nums1, nums2, k)
result

# %%
assert_kth_smallest_product(result, expected)
