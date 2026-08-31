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
from helpers import assert_get_maximum_gold, run_get_maximum_gold
from solution import Solution

# %%
# Example test case
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
expected = 24

# %%
result = run_get_maximum_gold(Solution, grid)
result

# %%
assert_get_maximum_gold(result, expected)
