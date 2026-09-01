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
from helpers import assert_max_points, run_max_points
from solution import Solution

# %%
# Example test case
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
expected = [5, 8, 1]

# %%
result = run_max_points(Solution, grid, queries)
result

# %%
assert_max_points(result, expected)
