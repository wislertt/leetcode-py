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
from helpers import assert_super_palindromes_in_range, run_super_palindromes_in_range
from solution import Solution

# %%
# Example test case
left = "4"
right = "1000"
expected = 4

# %%
result = run_super_palindromes_in_range(Solution, left, right)
result

# %%
assert_super_palindromes_in_range(result, expected)
