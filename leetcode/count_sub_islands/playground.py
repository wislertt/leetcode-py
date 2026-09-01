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
from helpers import assert_count_sub_islands, run_count_sub_islands
from solution import Solution

# %%
# Example test case
grid1 = [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
grid2 = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
expected = 2

# %%
result = run_count_sub_islands(Solution, grid1, grid2)
result

# %%
assert_count_sub_islands(result, expected)
