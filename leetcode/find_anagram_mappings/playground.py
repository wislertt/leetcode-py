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
from helpers import assert_anagram_mappings, run_anagram_mappings
from solution import Solution

# %%
# Example test case
nums1 = [12, 28, 46, 32, 50]
nums2 = [50, 12, 32, 46, 28]
expected = [1, 4, 3, 2, 0]

# %%
result = run_anagram_mappings(Solution, nums1, nums2)
result

# %%
assert_anagram_mappings(result, expected)
