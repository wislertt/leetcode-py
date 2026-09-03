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
from helpers import assert_replace_words, run_replace_words
from solution import Solution

# %%
# Example test case
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
expected = "the cat was rat by the bat"

# %%
result = run_replace_words(Solution, dictionary, sentence)
result

# %%
assert_replace_words(result, expected)
