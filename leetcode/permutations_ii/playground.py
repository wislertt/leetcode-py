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
from helpers import assert_permute_unique, run_permute_unique
from solution import Solution

# %%
# Example test case
nums = [1, 1, 2]
expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]

# %%
result = run_permute_unique(Solution, nums)
result

# %%
assert_permute_unique(result, expected)
