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
from helpers import assert_shopping_offers, run_shopping_offers
from solution import Solution

# %%
# Example test case
price = [2, 5]
special = [[3, 0, 5], [1, 2, 10]]
needs = [3, 2]
expected = 14

# %%
result = run_shopping_offers(Solution, price, special, needs)
result

# %%
assert_shopping_offers(result, expected)
