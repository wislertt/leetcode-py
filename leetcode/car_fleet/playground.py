# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_car_fleet, run_car_fleet
from solution import Solution

# %%
# Example test case
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
expected = 3

# %%
result = run_car_fleet(Solution, target, position, speed)
result

# %%
assert_car_fleet(result, expected)
