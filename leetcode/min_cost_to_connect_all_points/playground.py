# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_cost_connect_points, run_min_cost_connect_points
from solution import Solution

# %%
# Example test case
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
expected = 20

# %%
result = run_min_cost_connect_points(Solution, points)
result

# %%
assert_min_cost_connect_points(result, expected)
