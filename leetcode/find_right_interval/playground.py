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
from helpers import assert_find_right_interval, run_find_right_interval
from solution import Solution

# %%
# Example test case
intervals = [[3, 4], [2, 3], [1, 2]]
expected = [-1, 0, 1]

# %%
result = run_find_right_interval(Solution, intervals)
result

# %%
assert_find_right_interval(result, expected)
