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
from helpers import assert_count_numbers_with_unique_digits, run_count_numbers_with_unique_digits
from solution import Solution

# %%
# Example test case
n = 2
expected = 91

# %%
result = run_count_numbers_with_unique_digits(Solution, n)
result

# %%
assert_count_numbers_with_unique_digits(result, expected)
