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
from helpers import assert_pour_water, run_pour_water
from solution import Solution

# %%
# Example test case
heights = [2, 1, 1, 2, 1, 2, 2]
volume = 4
k = 3
expected = [2, 2, 2, 3, 2, 2, 2]

# %%
result = run_pour_water(Solution, heights, volume, k)
result

# %%
assert_pour_water(result, expected)
