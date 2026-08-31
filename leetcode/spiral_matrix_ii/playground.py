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
from helpers import assert_generate_matrix, run_generate_matrix
from solution import Solution

# %%
# Example test case
n = 3
expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

# %%
result = run_generate_matrix(Solution, n)
result

# %%
assert_generate_matrix(result, expected)
