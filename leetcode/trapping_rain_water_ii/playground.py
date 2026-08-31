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
from helpers import assert_trap_rain_water, run_trap_rain_water
from solution import Solution

# %%
# Example test case
height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
expected = 4

# %%
result = run_trap_rain_water(Solution, height_map)
result

# %%
assert_trap_rain_water(result, expected)
