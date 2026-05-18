# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_update_matrix, run_update_matrix
from solution import Solution

# %%
# Example test case
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

# %%
result = run_update_matrix(Solution, mat)
result

# %%
assert_update_matrix(result, expected)
