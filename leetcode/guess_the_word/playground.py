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
from helpers import assert_find_secret_word, run_find_secret_word
from solution import Solution

# %%
# Example test case
secret = "acckzz"
words = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
allowed_guesses = 10
expected = True

# %%
result = run_find_secret_word(Solution, secret, words, allowed_guesses)
result

# %%
assert_find_secret_word(result, expected)
