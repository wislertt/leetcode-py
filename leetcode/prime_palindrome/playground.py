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
from helpers import assert_prime_palindrome, run_prime_palindrome
from solution import Solution

# %%
# Example test case
n: int = 6
expected: int = 7

# %%
result = run_prime_palindrome(Solution, n)
result

# %%
assert_prime_palindrome(result, expected)
