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
from helpers import assert_matrix_reshape, run_matrix_reshape
from solution import Solution

# %%
# Example test case
mat = [[1, 2], [3, 4]]
r = 1
c = 4
expected = [[1, 2, 3, 4]]

# %%
result = run_matrix_reshape(Solution, mat, r, c)
result

# %%
assert_matrix_reshape(result, expected)
