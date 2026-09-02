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
from helpers import assert_find_maximum_xor, run_find_maximum_xor
from solution import Solution

# %%
# Example test case
nums = [3, 10, 5, 25, 2, 8]
expected = 28

# %%
result = run_find_maximum_xor(Solution, nums)
result

# %%
assert_find_maximum_xor(result, expected)
