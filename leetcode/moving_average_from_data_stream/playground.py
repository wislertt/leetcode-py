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
from helpers import assert_moving_average, run_moving_average
from solution import MovingAverage

# %%
# Example test case
operations = ["MovingAverage", "next", "next", "next", "next"]
inputs = [[3], [1], [10], [3], [5]]
expected = [None, 1.0, 5.5, 14 / 3, 6.0]

# %%
result, average = run_moving_average(MovingAverage, operations, inputs)
print(result)
average

# %%
assert_moving_average(result, expected)
