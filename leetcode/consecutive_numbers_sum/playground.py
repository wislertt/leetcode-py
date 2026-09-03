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
from helpers import assert_consecutive_numbers_sum, run_consecutive_numbers_sum
from solution import Solution

# %%
# Example test case
n = 9
expected = 3

# %%
result = run_consecutive_numbers_sum(Solution, n)
result

# %%
assert_consecutive_numbers_sum(result, expected)
