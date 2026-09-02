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
from helpers import assert_find_missing_and_repeated_values, run_find_missing_and_repeated_values
from solution import Solution

# %%
# Example test case
grid: list[list[int]] = [[1, 3], [2, 2]]
expected: list[int] = [2, 4]

# %%
result = run_find_missing_and_repeated_values(Solution, grid)
result

# %%
assert_find_missing_and_repeated_values(result, expected)
