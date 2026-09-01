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
from helpers import assert_max_score, run_max_score
from solution import Solution

# %%
# Example test case
nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
expected = 12

# %%
result = run_max_score(Solution, nums1, nums2, k)
result

# %%
assert_max_score(result, expected)
