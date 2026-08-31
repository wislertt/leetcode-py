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
from helpers import assert_maximum_minimum_path, run_maximum_minimum_path
from solution import Solution

# %%
# Example test case
grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
expected = 4

# %%
result = run_maximum_minimum_path(Solution, grid)
result

# %%
assert_maximum_minimum_path(result, expected)
