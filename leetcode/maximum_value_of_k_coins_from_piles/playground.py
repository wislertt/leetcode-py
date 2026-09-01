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
from helpers import assert_max_value_of_coins, run_max_value_of_coins
from solution import Solution

# %%
# Example test case
piles = [[1, 100, 3], [7, 8, 9]]
k = 2
expected = 101

# %%
result = run_max_value_of_coins(Solution, piles, k)
result

# %%
assert_max_value_of_coins(result, expected)
