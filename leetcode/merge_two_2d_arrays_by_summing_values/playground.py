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
from helpers import assert_merge_arrays, run_merge_arrays
from solution import Solution

# %%
# Example test case
nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]
expected = [[1, 6], [2, 3], [3, 2], [4, 6]]

# %%
result = run_merge_arrays(Solution, nums1, nums2)
result

# %%
assert_merge_arrays(result, expected)
