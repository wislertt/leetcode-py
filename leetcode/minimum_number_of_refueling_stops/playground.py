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
from helpers import assert_min_refuel_stops, run_min_refuel_stops
from solution import Solution

# %%
# Example test case
target = 100
start_fuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
expected = 2

# %%
result = run_min_refuel_stops(Solution, target, start_fuel, stations)
result

# %%
assert_min_refuel_stops(result, expected)
