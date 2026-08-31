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
from helpers import assert_num_tile_possibilities, run_num_tile_possibilities
from solution import Solution

# %%
# Example test case
tiles = "AAB"
expected = 8

# %%
result = run_num_tile_possibilities(Solution, tiles)
result

# %%
assert_num_tile_possibilities(result, expected)
