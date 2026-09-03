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
from helpers import assert_largest_time_from_digits, run_largest_time_from_digits
from solution import Solution

# %%
# Example test case
arr = [1, 2, 3, 4]
expected = "23:41"

# %%
result = run_largest_time_from_digits(Solution, arr)
result

# %%
assert_largest_time_from_digits(result, expected)
