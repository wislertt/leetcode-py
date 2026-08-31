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
from helpers import assert_words_typing, run_words_typing
from solution import Solution

# %%
# Example test case
sentence = ["hello", "world"]
rows = 2
cols = 8
expected = 1

# %%
result = run_words_typing(Solution, sentence, rows, cols)
result

# %%
assert_words_typing(result, expected)
