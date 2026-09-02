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
from helpers import assert_buy_choco, run_buy_choco
from solution import Solution

# %%
# Example test case
prices = [1, 2, 2]
money = 3
expected = 0

# %%
result = run_buy_choco(Solution, prices, money)
result

# %%
assert_buy_choco(result, expected)
