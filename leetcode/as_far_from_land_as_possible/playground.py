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
from helpers import assert_max_distance, run_max_distance
from solution import Solution

# %%
# Example test case
grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
expected = 2

# %%
result = run_max_distance(Solution, grid)
result

# %%
assert_max_distance(result, expected)
