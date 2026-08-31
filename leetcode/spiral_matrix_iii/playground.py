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
from helpers import assert_spiral_matrix_iii, run_spiral_matrix_iii
from solution import Solution

# %%
# Example test case
rows = 1
cols = 4
r_start = 0
c_start = 0
expected = [[0, 0], [0, 1], [0, 2], [0, 3]]

# %%
result = run_spiral_matrix_iii(Solution, rows, cols, r_start, c_start)
result

# %%
assert_spiral_matrix_iii(result, expected)
