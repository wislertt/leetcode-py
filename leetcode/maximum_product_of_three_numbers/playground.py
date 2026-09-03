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
from helpers import assert_maximum_product, run_maximum_product
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4]
expected = 24

# %%
result = run_maximum_product(Solution, nums)
result

# %%
assert_maximum_product(result, expected)
