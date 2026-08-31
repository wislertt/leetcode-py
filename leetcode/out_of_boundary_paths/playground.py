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
from helpers import assert_find_paths, run_find_paths
from solution import Solution

# %%
# Example test case
m = 2
n = 2
max_move = 2
start_row = 0
start_column = 0
expected = 6

# %%
result = run_find_paths(Solution, m, n, max_move, start_row, start_column)
result

# %%
assert_find_paths(result, expected)
