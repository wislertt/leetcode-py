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
from helpers import assert_min_time, run_min_time
from solution import Solution

# %%
# Example test case
n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
has_apple = [False, False, True, False, True, True, False]
expected = 8

# %%
result = run_min_time(Solution, n, edges, has_apple)
result

# %%
assert_min_time(result, expected)
