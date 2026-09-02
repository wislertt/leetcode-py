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
from helpers import assert_intersect, run_intersect
from solution import Solution

# %%
# Example test case (each grid is turned into a quad-tree by the helper)
grid1 = [[0, 1], [1, 0]]
grid2 = [[1, 0], [0, 1]]
expected = [[1, 1], [1, 1]]

# %%
result = run_intersect(Solution, grid1, grid2)
result

# %%
assert_intersect(result, expected)
