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
from helpers import assert_min_patches, run_min_patches
from solution import Solution

# %%
# Example test case
nums = [1, 3]
n = 6
expected = 1

# %%
result = run_min_patches(Solution, nums, n)
result

# %%
assert_min_patches(result, expected)
