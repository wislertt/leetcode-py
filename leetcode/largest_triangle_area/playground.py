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
from helpers import assert_largest_triangle_area, run_largest_triangle_area
from solution import Solution

# %%
# Example test case
points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
expected = 2.0

# %%
result = run_largest_triangle_area(Solution, points)
result

# %%
assert_largest_triangle_area(result, expected)
