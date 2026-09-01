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
from helpers import assert_find_buildings, run_find_buildings
from solution import Solution

# %%
# Example test case
heights = [4, 2, 3, 1]
expected = [0, 2, 3]

# %%
result = run_find_buildings(Solution, heights)
result

# %%
assert_find_buildings(result, expected)
