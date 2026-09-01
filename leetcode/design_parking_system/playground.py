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
from helpers import assert_parking_system, run_parking_system
from solution import ParkingSystem

# %%
# Example test case
operations = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
inputs = [[1, 1, 0], [1], [2], [3], [1]]
expected = [None, True, True, False, False]

# %%
result, system = run_parking_system(ParkingSystem, operations, inputs)
print(result)
system

# %%
assert_parking_system(result, expected)
