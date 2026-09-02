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
from helpers import assert_num_identical_pairs, run_num_identical_pairs
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 1, 1, 3]
expected = 4

# %%
result = run_num_identical_pairs(Solution, nums)
result

# %%
assert_num_identical_pairs(result, expected)
