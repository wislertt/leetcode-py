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
from helpers import assert_count_palindromic_subsequences, run_count_palindromic_subsequences
from solution import Solution

# %%
# Example test case
s = "bccb"
expected = 6

# %%
result = run_count_palindromic_subsequences(Solution, s)
result

# %%
assert_count_palindromic_subsequences(result, expected)
