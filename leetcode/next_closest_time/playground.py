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
from helpers import assert_next_closest_time, run_next_closest_time
from solution import Solution

# %%
# Example test case
time = "19:34"
expected = "19:39"

# %%
result = run_next_closest_time(Solution, time)
result

# %%
assert_next_closest_time(result, expected)
