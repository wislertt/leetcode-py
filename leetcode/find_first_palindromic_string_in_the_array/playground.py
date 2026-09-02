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
from helpers import assert_first_palindrome, run_first_palindrome
from solution import Solution

# %%
# Example test case
words = ["abc", "car", "ada", "racecar", "cool"]
expected = "ada"

# %%
result = run_first_palindrome(Solution, words)
result

# %%
assert_first_palindrome(result, expected)
