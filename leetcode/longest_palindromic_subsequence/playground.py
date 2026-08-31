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
from helpers import assert_longest_palindrome_subseq, run_longest_palindrome_subseq
from solution import Solution

# %%
# Example test case
s = "bbbab"
expected = 4

# %%
result = run_longest_palindrome_subseq(Solution, s)
result

# %%
assert_longest_palindrome_subseq(result, expected)
