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
from helpers import assert_count_digit_one, run_count_digit_one
from solution import Solution

# %%
# Example test case
n: int = 13
expected: int = 6

# %%
result = run_count_digit_one(Solution, n)
result

# %%
assert_count_digit_one(result, expected)
