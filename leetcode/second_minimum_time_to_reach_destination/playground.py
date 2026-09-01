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
from helpers import assert_second_minimum, run_second_minimum
from solution import Solution

# %%
# Example test case
n = 5
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
time = 3
change = 5
expected = 13

# %%
result = run_second_minimum(Solution, n, edges, time, change)
result

# %%
assert_second_minimum(result, expected)
