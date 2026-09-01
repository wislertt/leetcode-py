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
from helpers import assert_minimum_time, run_minimum_time
from solution import Solution

# %%
# Example test case
grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
expected = 7

# %%
result = run_minimum_time(Solution, grid)
result

# %%
assert_minimum_time(result, expected)
