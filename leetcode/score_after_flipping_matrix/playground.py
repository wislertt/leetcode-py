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
from helpers import assert_matrix_score, run_matrix_score
from solution import Solution

# %%
# Example test case
grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
expected = 39

# %%
result = run_matrix_score(Solution, grid)
result

# %%
assert_matrix_score(result, expected)
