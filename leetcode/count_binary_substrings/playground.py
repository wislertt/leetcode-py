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
from helpers import assert_count_binary_substrings, run_count_binary_substrings
from solution import Solution

# %%
# Example test case
s = "00110011"
expected = 6

# %%
result = run_count_binary_substrings(Solution, s)
result

# %%
assert_count_binary_substrings(result, expected)
