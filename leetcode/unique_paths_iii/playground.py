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
from helpers import assert_unique_paths_iii, run_unique_paths_iii
from solution import Solution

# %%
# Example test case
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
expected = 2

# %%
result = run_unique_paths_iii(Solution, grid)
result

# %%
assert_unique_paths_iii(result, expected)
