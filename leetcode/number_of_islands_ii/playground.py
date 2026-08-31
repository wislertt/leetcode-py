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
from helpers import assert_num_islands2, run_num_islands2
from solution import Solution

# %%
# Example test case
m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
expected = [1, 1, 2, 3]

# %%
result = run_num_islands2(Solution, m, n, positions)
result

# %%
assert_num_islands2(result, expected)
