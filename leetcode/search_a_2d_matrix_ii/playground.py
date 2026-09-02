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
from helpers import assert_search_matrix, run_search_matrix
from solution import Solution

# %%
# Example test case
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]]
target = 5
expected = True

# %%
result = run_search_matrix(Solution, matrix, target)
result

# %%
assert_search_matrix(result, expected)
