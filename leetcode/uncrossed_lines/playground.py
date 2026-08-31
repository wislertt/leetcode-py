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
from helpers import assert_max_uncrossed_lines, run_max_uncrossed_lines
from solution import Solution

# %%
# Example test case
nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
expected = 2

# %%
result = run_max_uncrossed_lines(Solution, nums1, nums2)
result

# %%
assert_max_uncrossed_lines(result, expected)
