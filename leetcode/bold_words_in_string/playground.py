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
from helpers import assert_bold_words, run_bold_words
from solution import Solution

# %%
# Example test case
words = ["ab", "bc"]
s = "aabcd"
expected = "a<b>abc</b>d"

# %%
result = run_bold_words(Solution, words, s)
result

# %%
assert_bold_words(result, expected)
