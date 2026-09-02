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
from helpers import assert_spiral_matrix, run_spiral_matrix
from solution import Solution

# %%
# Example test case
m = 3
n = 5
head_vals = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
expected = [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]

# %%
result = run_spiral_matrix(Solution, m, n, head_vals)
result

# %%
assert_spiral_matrix(result, expected)
