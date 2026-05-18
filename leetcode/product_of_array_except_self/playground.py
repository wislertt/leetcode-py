# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_product_except_self, run_product_except_self
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4]
expected = [24, 12, 8, 6]

# %%
result = run_product_except_self(Solution, nums)
result

# %%
assert_product_except_self(result, expected)
