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
from helpers import assert_interval_intersection, run_interval_intersection
from solution import Solution

# %%
# Example test case
first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

# %%
result = run_interval_intersection(Solution, first_list, second_list)
result

# %%
assert_interval_intersection(result, expected)
