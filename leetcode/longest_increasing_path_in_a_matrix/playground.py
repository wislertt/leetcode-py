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
from helpers import assert_longest_increasing_path, run_longest_increasing_path
from solution import Solution

# %%
# Example test case
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
expected = 4

# %%
result = run_longest_increasing_path(Solution, matrix)
result

# %%
assert_longest_increasing_path(result, expected)
