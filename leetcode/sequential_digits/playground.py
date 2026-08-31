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
from helpers import assert_sequential_digits, run_sequential_digits
from solution import Solution

# %%
# Example test case
low = 100
high = 300
expected = [123, 234]

# %%
result = run_sequential_digits(Solution, low, high)
result

# %%
assert_sequential_digits(result, expected)
