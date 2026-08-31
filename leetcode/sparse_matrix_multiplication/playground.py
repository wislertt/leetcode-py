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
from helpers import assert_multiply, run_multiply
from solution import Solution

# %%
# Example test case
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
expected = [[7, 0, 0], [-7, 0, 3]]

# %%
result = run_multiply(Solution, mat1, mat2)
result

# %%
assert_multiply(result, expected)
