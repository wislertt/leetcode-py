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
from helpers import assert_tuple_same_product, run_tuple_same_product
from solution import Solution

# %%
# Example test case
nums = [2, 3, 4, 6]
expected = 8

# %%
result = run_tuple_same_product(Solution, nums)
result

# %%
assert_tuple_same_product(result, expected)
