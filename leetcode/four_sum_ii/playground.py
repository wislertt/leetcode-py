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
from helpers import assert_four_sum_count, run_four_sum_count
from solution import Solution

# %%
# Example test case
nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
expected = 2

# %%
result = run_four_sum_count(Solution, nums1, nums2, nums3, nums4)
result

# %%
assert_four_sum_count(result, expected)
