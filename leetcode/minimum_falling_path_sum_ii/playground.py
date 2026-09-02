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
from helpers import assert_min_falling_path_sum, run_min_falling_path_sum
from solution import Solution

# %%
# Example test case
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = 13

# %%
result = run_min_falling_path_sum(Solution, grid)
result

# %%
assert_min_falling_path_sum(result, expected)
