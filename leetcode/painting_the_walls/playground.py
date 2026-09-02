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
from helpers import assert_paint_walls, run_paint_walls
from solution import Solution

# %%
# Example test case
cost = [1, 2, 3, 2]
time = [1, 2, 3, 2]
expected = 3

# %%
result = run_paint_walls(Solution, cost, time)
result

# %%
assert_paint_walls(result, expected)
