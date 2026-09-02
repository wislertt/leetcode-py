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
from helpers import assert_largest_local, run_largest_local
from solution import Solution

# %%
# Example test case
grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
expected = [[9, 9], [8, 6]]

# %%
result = run_largest_local(Solution, grid)
result

# %%
assert_largest_local(result, expected)
