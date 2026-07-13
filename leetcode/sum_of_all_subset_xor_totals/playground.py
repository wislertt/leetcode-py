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
from helpers import assert_subset_xor_sum, run_subset_xor_sum
from solution import Solution

# %%
# Example test case
nums = [1, 3]
expected = 6

# %%
result = run_subset_xor_sum(Solution, nums)
result

# %%
assert_subset_xor_sum(result, expected)
