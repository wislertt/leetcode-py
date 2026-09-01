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
from helpers import assert_minimum_fuel_cost, run_minimum_fuel_cost
from solution import Solution

# %%
# Example test case
roads = [[0, 1], [0, 2], [0, 3]]
seats = 5
expected = 3

# %%
result = run_minimum_fuel_cost(Solution, roads, seats)
result

# %%
assert_minimum_fuel_cost(result, expected)
