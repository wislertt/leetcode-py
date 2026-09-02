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
from helpers import assert_get_maximum_xor, run_get_maximum_xor
from solution import Solution

# %%
# Example test case
nums = [0, 1, 1, 3]
maximum_bit = 2
expected = [0, 3, 2, 3]

# %%
result = run_get_maximum_xor(Solution, nums, maximum_bit)
result

# %%
assert_get_maximum_xor(result, expected)
