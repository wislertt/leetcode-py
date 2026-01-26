# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_min_path_sum, run_min_path_sum
from solution import Solution

# %%
# Example test case
grid: list[list[int]] = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
expected = 7

# %%
result = run_min_path_sum(Solution, grid)
result

# %%
assert_min_path_sum(result, expected)
