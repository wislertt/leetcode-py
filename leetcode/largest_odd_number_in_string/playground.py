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
from helpers import assert_largest_odd_number, run_largest_odd_number
from solution import Solution

# %%
# Example test case
num = "52"
expected = "5"

# %%
result = run_largest_odd_number(Solution, num)
result

# %%
assert_largest_odd_number(result, expected)
