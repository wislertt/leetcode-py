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
from helpers import assert_count_corner_rectangles, run_count_corner_rectangles
from solution import Solution

# %%
# Example test case
grid = [[1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]
expected = 1

# %%
result = run_count_corner_rectangles(Solution, grid)
result

# %%
assert_count_corner_rectangles(result, expected)
