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
from helpers import assert_cal_points, run_cal_points
from solution import Solution

# %%
# Example test case
operations = ["5", "2", "C", "D", "+"]
expected = 30

# %%
result = run_cal_points(Solution, operations)
result

# %%
assert_cal_points(result, expected)
