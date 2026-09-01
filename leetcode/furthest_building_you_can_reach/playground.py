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
from helpers import assert_furthest_building, run_furthest_building
from solution import Solution

# %%
# Example test case
heights = [4, 2, 7, 6, 9, 14, 12]
bricks = 5
ladders = 1
expected = 4

# %%
result = run_furthest_building(Solution, heights, bricks, ladders)
result

# %%
assert_furthest_building(result, expected)
