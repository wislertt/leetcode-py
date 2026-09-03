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
from helpers import assert_intersection_size_two, run_intersection_size_two
from solution import Solution

# %%
# Example test case
intervals = [[1, 3], [3, 7], [8, 9]]
expected = 5

# %%
result = run_intersection_size_two(Solution, intervals)
result

# %%
assert_intersection_size_two(result, expected)
