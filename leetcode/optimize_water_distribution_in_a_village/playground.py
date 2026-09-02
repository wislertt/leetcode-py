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
from helpers import assert_min_cost_to_supply_water, run_min_cost_to_supply_water
from solution import Solution

# %%
# Example test case
n = 3
wells = [1, 2, 2]
pipes = [[1, 2, 1], [2, 3, 1]]
expected = 3

# %%
result = run_min_cost_to_supply_water(Solution, n, wells, pipes)
result

# %%
assert_min_cost_to_supply_water(result, expected)
