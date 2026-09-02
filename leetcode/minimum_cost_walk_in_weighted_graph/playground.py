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
n = 5
edges = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
query = [[0, 3], [3, 4]]
expected = [1, -1]

# %%
result = run_minimum_cost(Solution, n, edges, query)
result

# %%
assert_minimum_cost(result, expected)
