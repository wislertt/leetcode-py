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
from helpers import assert_add_digits, run_add_digits
from solution import Solution

# %%
# Example test case
num = 38
expected = 2

# %%
result = run_add_digits(Solution, num)
result

# %%
assert_add_digits(result, expected)
