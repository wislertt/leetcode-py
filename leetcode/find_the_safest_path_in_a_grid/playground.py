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
from helpers import assert_maximum_safeness_factor, run_maximum_safeness_factor
from solution import Solution

# %%
# Example test case
grid: list[list[int]] = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
expected = 2

# %%
result = run_maximum_safeness_factor(Solution, grid)
result

# %%
assert_maximum_safeness_factor(result, expected)
