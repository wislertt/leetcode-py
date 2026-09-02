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
from helpers import assert_can_measure_water, run_can_measure_water
from solution import Solution

# %%
# Example test case
x = 3
y = 5
target = 4
expected = True

# %%
result = run_can_measure_water(Solution, x, y, target)
result

# %%
assert_can_measure_water(result, expected)
