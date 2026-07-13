# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_unique_paths_with_obstacles, run_unique_paths_with_obstacles
from solution import Solution

# %%
# Example test case
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
expected = 2

# %%
result = run_unique_paths_with_obstacles(Solution, grid)
result

# %%
assert_unique_paths_with_obstacles(result, expected)
