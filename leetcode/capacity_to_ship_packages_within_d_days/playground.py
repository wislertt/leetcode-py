# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_ship_within_days, run_ship_within_days
from solution import Solution

# %%
# Example test case
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
expected = 15

# %%
result = run_ship_within_days(Solution, weights, days)
result

# %%
assert_ship_within_days(result, expected)
