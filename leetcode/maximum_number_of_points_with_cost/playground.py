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
points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
expected = 9

# %%
result = run_max_points(Solution, points)
result

# %%
assert_max_points(result, expected)
