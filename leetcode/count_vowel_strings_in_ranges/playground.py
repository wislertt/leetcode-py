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
from helpers import assert_vowel_strings, run_vowel_strings
from solution import Solution

# %%
# Example test case
words: list[str] = ["aba", "bcb", "ece", "aa", "e"]
queries: list[list[int]] = [[0, 2], [1, 4], [1, 1]]
expected: list[int] = [2, 3, 0]

# %%
result = run_vowel_strings(Solution, words, queries)
result

# %%
assert_vowel_strings(result, expected)
