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
from helpers import assert_count_characters, run_count_characters
from solution import Solution

# %%
# Example test case
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
expected = 6

# %%
result = run_count_characters(Solution, words, chars)
result

# %%
assert_count_characters(result, expected)
