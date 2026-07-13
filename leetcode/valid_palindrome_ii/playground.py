# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_valid_palindrome, run_valid_palindrome
from solution import Solution

# %%
# Example test case
s = "abca"
expected = True

# %%
result = run_valid_palindrome(Solution, s)
result

# %%
assert_valid_palindrome(result, expected)
