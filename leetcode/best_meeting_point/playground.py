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
from helpers import assert_min_total_distance, run_min_total_distance
from solution import Solution

# %%
# Example test case
grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
expected = 6

# %%
result = run_min_total_distance(Solution, grid)
result

# %%
assert_min_total_distance(result, expected)
