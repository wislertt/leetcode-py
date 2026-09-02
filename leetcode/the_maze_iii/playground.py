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
from helpers import assert_find_shortest_way, run_find_shortest_way
from solution import Solution

# %%
# Example test case
maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
ball = [4, 3]
hole = [0, 1]
expected = "lul"

# %%
result = run_find_shortest_way(Solution, maze, ball, hole)
result

# %%
assert_find_shortest_way(result, expected)
