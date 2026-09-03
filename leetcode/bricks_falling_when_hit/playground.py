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
from helpers import assert_hit_bricks, run_hit_bricks
from solution import Solution

# %%
# Example test case
grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
hits = [[1, 0]]
expected = [2]

# %%
result = run_hit_bricks(Solution, grid, hits)
result

# %%
assert_hit_bricks(result, expected)
