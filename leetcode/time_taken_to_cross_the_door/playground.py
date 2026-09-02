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
from helpers import assert_time_taken, run_time_taken
from solution import Solution

# %%
# Example test case
arrival = [0, 1, 1, 2, 4]
state = [0, 1, 0, 0, 1]
expected = [0, 3, 1, 2, 4]

# %%
result = run_time_taken(Solution, arrival, state)
result

# %%
assert_time_taken(result, expected)
