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
from helpers import assert_words_abbreviation, run_words_abbreviation
from solution import Solution

# %%
# Example test case
words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
expected = ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]

# %%
result = run_words_abbreviation(Solution, words)
result

# %%
assert_words_abbreviation(result, expected)
