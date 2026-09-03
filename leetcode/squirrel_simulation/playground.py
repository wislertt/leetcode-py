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
from helpers import assert_min_distance, run_min_distance
from solution import Solution

# %%
# Example test case
height = 5
width = 7
tree = [2, 2]
squirrel = [4, 4]
nuts = [[3, 0], [2, 5]]
expected = 12

# %%
result = run_min_distance(Solution, height, width, tree, squirrel, nuts)
result

# %%
assert_min_distance(result, expected)
