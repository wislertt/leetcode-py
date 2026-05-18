# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_longest_palindrome, run_longest_palindrome
from solution import Solution

# %%
# Example test case
s = "abccccdd"
expected = 7

# %%
result = run_longest_palindrome(Solution, s)
result

# %%
assert_longest_palindrome(result, expected)
