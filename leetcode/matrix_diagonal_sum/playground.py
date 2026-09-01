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
from helpers import assert_diagonal_sum, run_diagonal_sum
from solution import Solution

# %%
# Example test case
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = 25

# %%
result = run_diagonal_sum(Solution, mat)
result

# %%
assert_diagonal_sum(result, expected)
