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
from helpers import assert_repair_cars, run_repair_cars
from solution import Solution

# %%
# Example test case
ranks = [4, 2, 3, 1]
cars = 10
expected = 16

# %%
result = run_repair_cars(Solution, ranks, cars)
result

# %%
assert_repair_cars(result, expected)
