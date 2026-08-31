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
from helpers import assert_can_permute_palindrome, run_can_permute_palindrome
from solution import Solution

# %%
# Example test case
s = "carerac"
expected = True

# %%
result = run_can_permute_palindrome(Solution, s)
result

# %%
assert_can_permute_palindrome(result, expected)
