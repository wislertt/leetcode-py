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
from helpers import assert_number_of_substrings, run_number_of_substrings
from solution import Solution

# %%
# Example test case
s = "abcabc"
expected = 10

# %%
result = run_number_of_substrings(Solution, s)
result

# %%
assert_number_of_substrings(result, expected)
