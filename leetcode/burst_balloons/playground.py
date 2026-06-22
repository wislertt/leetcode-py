# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_max_coins, run_max_coins
from solution import Solution

# %%
# Example test case
nums = [3, 1, 5, 8]
expected = 167

# %%
result = run_max_coins(Solution, nums)
result

# %%
assert_max_coins(result, expected)
