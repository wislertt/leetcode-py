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
from helpers import assert_minimum_one_bit_operations, run_minimum_one_bit_operations
from solution import Solution

# %%
# Example test case
n = 6
expected = 4

# %%
result = run_minimum_one_bit_operations(Solution, n)
result

# %%
assert_minimum_one_bit_operations(result, expected)
