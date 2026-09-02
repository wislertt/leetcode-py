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
from helpers import assert_k_smallest_pairs, run_k_smallest_pairs
from solution import Solution

# %%
# Example test case
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
expected = [[1, 2], [1, 4], [1, 6]]

# %%
result = run_k_smallest_pairs(Solution, nums1, nums2, k)
result

# %%
assert_k_smallest_pairs(result, expected)
