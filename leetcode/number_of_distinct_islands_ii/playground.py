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
from helpers import assert_num_distinct_islands_ii, run_num_distinct_islands_ii
from solution import Solution

# %%
# Example test case
grid = [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]]
expected = 1

# %%
result = run_num_distinct_islands_ii(Solution, grid)
result

# %%
assert_num_distinct_islands_ii(result, expected)
