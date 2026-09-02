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
from helpers import assert_calculate_time, run_calculate_time
from solution import Solution

# %%
# Example test case
keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
expected = 4

# %%
result = run_calculate_time(Solution, keyboard, word)
result

# %%
assert_calculate_time(result, expected)
