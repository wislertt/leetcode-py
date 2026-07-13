# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_transpose, run_transpose
from solution import Solution

# %%
# Example test case
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# %%
result = run_transpose(Solution, matrix)
result

# %%
assert_transpose(result, expected)
