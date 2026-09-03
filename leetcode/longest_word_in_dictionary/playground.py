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
from helpers import assert_longest_word, run_longest_word
from solution import Solution

# %%
# Example test case
words = ["w", "wo", "wor", "worl", "world"]
expected = "world"

# %%
result = run_longest_word(Solution, words)
result

# %%
assert_longest_word(result, expected)
