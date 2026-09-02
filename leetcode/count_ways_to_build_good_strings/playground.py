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
from helpers import assert_count_good_strings, run_count_good_strings
from solution import Solution

# %%
# Example test case
low = 3
high = 3
zero = 1
one = 1
expected = 8

# %%
result = run_count_good_strings(Solution, low, high, zero, one)
result

# %%
assert_count_good_strings(result, expected)
