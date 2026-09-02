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
from helpers import assert_max_product_difference, run_max_product_difference
from solution import Solution

# %%
# Example test case
nums = [5, 6, 2, 7, 4]
expected = 34

# %%
result = run_max_product_difference(Solution, nums)
result

# %%
assert_max_product_difference(result, expected)
