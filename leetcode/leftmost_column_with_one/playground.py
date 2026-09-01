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
from helpers import assert_leftmost_column_with_one, run_leftmost_column_with_one
from solution import Solution

# %%
# Example test case
mat = [[0, 0], [0, 1]]
expected = 1

# %%
result, get_calls = run_leftmost_column_with_one(Solution, mat)
print(get_calls)
result

# %%
assert_leftmost_column_with_one((result, get_calls), expected)
