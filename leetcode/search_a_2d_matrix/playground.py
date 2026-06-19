# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_search_matrix, run_search_matrix
from solution import Solution

# %%
# Example test case
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
expected = True

# %%
result = run_search_matrix(Solution, matrix, target)
result

# %%
assert_search_matrix(result, expected)
