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
from helpers import assert_at_most_n_given_digit_set, run_at_most_n_given_digit_set
from solution import Solution

# %%
# Example test case
digits = ["1", "3", "5", "7"]
n = 100
expected = 20

# %%
result = run_at_most_n_given_digit_set(Solution, digits, n)
result

# %%
assert_at_most_n_given_digit_set(result, expected)
