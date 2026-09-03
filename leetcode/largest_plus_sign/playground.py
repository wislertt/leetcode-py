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
from helpers import assert_order_of_largest_plus_sign, run_order_of_largest_plus_sign
from solution import Solution

# %%
# Example test case
n = 5
mines = [[4, 2]]
expected = 2

# %%
result = run_order_of_largest_plus_sign(Solution, n, mines)
result

# %%
assert_order_of_largest_plus_sign(result, expected)
