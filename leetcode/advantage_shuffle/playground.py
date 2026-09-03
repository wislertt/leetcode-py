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
from helpers import assert_advantage_count, run_advantage_count
from solution import Solution

# %%
# Example test case
nums1 = [2, 7, 11, 15]
nums2 = [1, 10, 4, 11]
expected = 4

# %%
result = run_advantage_count(Solution, nums1, nums2)
print(result)
result

# %%
assert_advantage_count(result, expected)
