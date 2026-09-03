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
from helpers import assert_word_filter, run_word_filter
from solution import WordFilter

# %%
# Example test case
operations = ["WordFilter", "f"]
inputs = [["apple"], ["a", "e"]]
expected = [None, 0]

# %%
result, word_filter = run_word_filter(WordFilter, operations, inputs)
print(result)
word_filter

# %%
assert_word_filter(result, expected)
