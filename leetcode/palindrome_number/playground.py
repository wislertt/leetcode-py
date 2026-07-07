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
from helpers import assert_is_palindrome, run_is_palindrome
from solution import Solution

# %%
# Example test case
x = 121
expected = True

# %%
result = run_is_palindrome(Solution, x)
result

# %%
assert_is_palindrome(result, expected)
