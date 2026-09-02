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
from helpers import assert_find_nth_digit, run_find_nth_digit
from solution import Solution

# %%
# Example test case
n = 11
expected = 0

# %%
result = run_find_nth_digit(Solution, n)
result

# %%
assert_find_nth_digit(result, expected)
