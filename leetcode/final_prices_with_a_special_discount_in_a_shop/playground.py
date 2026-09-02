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
from helpers import assert_final_prices, run_final_prices
from solution import Solution

# %%
# Example test case
prices = [8, 4, 6, 2, 3]
expected = [4, 2, 4, 2, 3]

# %%
result = run_final_prices(Solution, prices)
result

# %%
assert_final_prices(result, expected)
