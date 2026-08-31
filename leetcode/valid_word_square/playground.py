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
from helpers import assert_valid_word_square, run_valid_word_square
from solution import Solution

# %%
# Example test case
words = ["abcd", "bnrt", "crmy", "dtye"]
expected = True

# %%
result = run_valid_word_square(Solution, words)
result

# %%
assert_valid_word_square(result, expected)
