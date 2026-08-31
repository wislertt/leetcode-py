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
from helpers import assert_max_equal_rows_after_flips, run_max_equal_rows_after_flips
from solution import Solution

# %%
# Example test case
matrix = [[0, 1], [1, 0]]
expected = 2

# %%
result = run_max_equal_rows_after_flips(Solution, matrix)
result

# %%
assert_max_equal_rows_after_flips(result, expected)
