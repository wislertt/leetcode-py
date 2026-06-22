# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_swim_in_water, run_swim_in_water
from solution import Solution

# %%
# Example test case
grid = [[0, 2], [1, 3]]
expected = 3

# %%
result = run_swim_in_water(Solution, grid)
result

# %%
assert_swim_in_water(result, expected)
