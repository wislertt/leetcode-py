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
from helpers import assert_projection_area, run_projection_area
from solution import Solution

# %%
# Example test case
grid = [[1, 2], [3, 4]]
expected = 17

# %%
result = run_projection_area(Solution, grid)
result

# %%
assert_projection_area(result, expected)
