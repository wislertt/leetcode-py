# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_word_break, run_word_break
from solution import Solution

# %%
# Example test case
s = "catsanddog"
word_dict = ["cat", "cats", "and", "sand", "dog"]
expected = ["cats and dog", "cat sand dog"]

# %%
result = run_word_break(Solution, s, word_dict)
result

# %%
assert_word_break(result, expected)
