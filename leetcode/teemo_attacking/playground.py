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
from helpers import assert_find_poisoned_duration, run_find_poisoned_duration
from solution import Solution

# %%
# Example test case
time_series: list[int] = [1, 4]
duration = 2
expected = 4

# %%
result = run_find_poisoned_duration(Solution, time_series, duration)
result

# %%
assert_find_poisoned_duration(result, expected)
