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
from helpers import assert_surface_area, run_surface_area
from solution import Solution

# %%
# Example test case
grid = [[1, 2], [3, 4]]
expected = 34

# %%
result = run_surface_area(Solution, grid)
result

# %%
assert_surface_area(result, expected)
