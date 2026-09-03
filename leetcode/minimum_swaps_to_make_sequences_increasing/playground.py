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
from helpers import assert_min_swap, run_min_swap
from solution import Solution

# %%
# Example test case
nums1 = [1, 3, 5, 4]
nums2 = [1, 2, 3, 7]
expected = 1

# %%
result = run_min_swap(Solution, nums1, nums2)
result

# %%
assert_min_swap(result, expected)
