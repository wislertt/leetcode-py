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
from helpers import assert_find_words, run_find_words
from solution import Solution

# %%
# Example test case
words: list[str] = ["Hello", "Alaska", "Dad", "Peace"]
expected: list[str] = ["Alaska", "Dad"]

# %%
result = run_find_words(Solution, words)
result

# %%
assert_find_words(result, expected)
