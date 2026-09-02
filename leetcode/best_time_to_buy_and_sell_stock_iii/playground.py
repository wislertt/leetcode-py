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
from helpers import assert_max_profit, run_max_profit
from solution import Solution

# %%
# Example test case
prices = [3, 3, 5, 0, 0, 3, 1, 4]
expected = 6

# %%
result = run_max_profit(Solution, prices)
result

# %%
assert_max_profit(result, expected)
