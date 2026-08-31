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
from helpers import assert_num_subarray_product_less_than_k, run_num_subarray_product_less_than_k
from solution import Solution

# %%
# Example test case
nums = [10, 5, 2, 6]
k = 100
expected = 8

# %%
result = run_num_subarray_product_less_than_k(Solution, nums, k)
result

# %%
assert_num_subarray_product_less_than_k(result, expected)
