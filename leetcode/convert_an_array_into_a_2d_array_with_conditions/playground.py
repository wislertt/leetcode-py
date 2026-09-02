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
from helpers import assert_find_matrix, run_find_matrix
from solution import Solution

# %%
# Example test case
nums = [1, 3, 4, 1, 2, 3, 1]
expected = sorted(nums)

# %%
result = run_find_matrix(Solution, nums)
result

# %%
assert_find_matrix(result, expected)
