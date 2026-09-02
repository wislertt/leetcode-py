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
from helpers import assert_calculate_minimum_hp, run_calculate_minimum_hp
from solution import Solution

# %%
# Example test case
dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
expected = 7

# %%
result = run_calculate_minimum_hp(Solution, dungeon)
result

# %%
assert_calculate_minimum_hp(result, expected)
