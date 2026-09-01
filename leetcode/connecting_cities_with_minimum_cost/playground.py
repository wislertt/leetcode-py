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
from helpers import assert_minimum_cost, run_minimum_cost
from solution import Solution

# %%
# Example test case
n = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
expected = 6

# %%
result = run_minimum_cost(Solution, n, connections)
result

# %%
assert_minimum_cost(result, expected)
