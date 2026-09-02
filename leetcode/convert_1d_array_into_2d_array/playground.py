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
from helpers import assert_construct_2d_array, run_construct_2d_array
from solution import Solution

# %%
# Example test case
original = [1, 2, 3, 4]
m = 2
n = 2
expected = [[1, 2], [3, 4]]

# %%
result = run_construct_2d_array(Solution, original, m, n)
result

# %%
assert_construct_2d_array(result, expected)
