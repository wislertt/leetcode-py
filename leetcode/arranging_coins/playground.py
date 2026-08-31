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
from helpers import assert_arrange_coins, run_arrange_coins
from solution import Solution

# %%
# Example test case
n = 5
expected = 2

# %%
result = run_arrange_coins(Solution, n)
result

# %%
assert_arrange_coins(result, expected)
