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
from helpers import assert_generate_palindromes, run_generate_palindromes
from solution import Solution

# %%
# Example test case
s = "aabb"
expected = ["abba", "baab"]

# %%
result = run_generate_palindromes(Solution, s)
result

# %%
assert_generate_palindromes(result, expected)
