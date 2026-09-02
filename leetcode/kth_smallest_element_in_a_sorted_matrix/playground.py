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
from helpers import assert_kth_smallest, run_kth_smallest
from solution import Solution

# %%
# Example test case
matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
expected = 13

# %%
result = run_kth_smallest(Solution, matrix, k)
result

# %%
assert_kth_smallest(result, expected)
