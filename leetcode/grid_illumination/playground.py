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
from helpers import assert_grid_illumination, run_grid_illumination
from solution import Solution

# %%
# Example test case
n = 5
lamps = [[0, 0], [4, 4]]
queries = [[1, 1], [1, 0]]
expected = [1, 0]

# %%
result = run_grid_illumination(Solution, n, lamps, queries)
result

# %%
assert_grid_illumination(result, expected)
