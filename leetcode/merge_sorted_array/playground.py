# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_merge, run_merge
from solution import Solution

# %%
# Example test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
expected = [1, 2, 2, 3, 5, 6]

# %%
result = run_merge(Solution, nums1, m, nums2, n)
result

# %%
assert_merge(result, expected)
