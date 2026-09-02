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
from helpers import assert_get_money_amount, run_get_money_amount
from solution import Solution

# %%
# Example test case
n = 10
expected = 16

# %%
result = run_get_money_amount(Solution, n)
result

# %%
assert_get_money_amount(result, expected)
