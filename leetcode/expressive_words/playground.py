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
from helpers import assert_expressive_words, run_expressive_words
from solution import Solution

# %%
# Example test case
s = "heeellooo"
words = ["hello", "hi", "helo"]
expected = 1

# %%
result = run_expressive_words(Solution, s, words)
result

# %%
assert_expressive_words(result, expected)
