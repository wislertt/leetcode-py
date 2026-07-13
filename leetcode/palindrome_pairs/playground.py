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
from helpers import assert_palindrome_pairs, run_palindrome_pairs
from solution import Solution

# %%
# Example test case
words = ["abcd", "dcba", "lls", "s", "sssll"]
expected = [[0, 1], [1, 0], [3, 2], [2, 4]]

# %%
result = run_palindrome_pairs(Solution, words)
result

# %%
assert_palindrome_pairs(result, expected)
