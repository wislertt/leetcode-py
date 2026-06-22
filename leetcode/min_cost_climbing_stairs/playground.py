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
from helpers import assert_min_cost_climbing_stairs, run_min_cost_climbing_stairs
from solution import Solution

# %%
# Example test case
cost = [10, 15, 20]
expected = 15

# %%
result = run_min_cost_climbing_stairs(Solution, cost)
result

# %%
assert_min_cost_climbing_stairs(result, expected)
