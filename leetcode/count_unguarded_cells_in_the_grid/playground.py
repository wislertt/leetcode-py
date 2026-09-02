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
from helpers import assert_count_unguarded, run_count_unguarded
from solution import Solution

# %%
# Example test case
m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]
expected = 7

# %%
result = run_count_unguarded(Solution, m, n, guards, walls)
result

# %%
assert_count_unguarded(result, expected)
