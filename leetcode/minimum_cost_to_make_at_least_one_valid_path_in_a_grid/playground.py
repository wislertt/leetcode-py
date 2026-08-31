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
from helpers import assert_min_cost, run_min_cost
from solution import Solution

# %%
# Example test case
grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
expected = 0

# %%
result = run_min_cost(Solution, grid)
result

# %%
assert_min_cost(result, expected)
