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
from helpers import assert_min_available_duration, run_min_available_duration
from solution import Solution

# %%
# Example test case
slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 8
expected = [60, 68]

# %%
result = run_min_available_duration(Solution, slots1, slots2, duration)
result

# %%
assert_min_available_duration(result, expected)
