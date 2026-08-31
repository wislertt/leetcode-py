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
from helpers import assert_min_k_bit_flips, run_min_k_bit_flips
from solution import Solution

# %%
# Example test case
nums = [0, 1, 0]
k = 1
expected = 2

# %%
result = run_min_k_bit_flips(Solution, nums, k)
result

# %%
assert_min_k_bit_flips(result, expected)
