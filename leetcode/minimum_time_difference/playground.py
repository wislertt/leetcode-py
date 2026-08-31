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
from helpers import assert_find_min_difference, run_find_min_difference
from solution import Solution

# %%
# Example test case
time_points = ["23:59", "00:00"]
expected = 1

# %%
result = run_find_min_difference(Solution, time_points)
result

# %%
assert_find_min_difference(result, expected)
