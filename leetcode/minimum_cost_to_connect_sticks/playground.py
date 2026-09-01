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
from helpers import assert_connect_sticks, run_connect_sticks
from solution import Solution

# %%
# Example test case
sticks = [2, 4, 3]
expected = 14

# %%
result = run_connect_sticks(Solution, sticks)
result

# %%
assert_connect_sticks(result, expected)
