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
from helpers import assert_least_bricks, run_least_bricks
from solution import Solution

# %%
# Example test case
wall: list[list[int]] = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
expected = 2

# %%
result = run_least_bricks(Solution, wall)
result

# %%
assert_least_bricks(result, expected)
