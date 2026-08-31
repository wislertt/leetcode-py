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
from helpers import assert_word_subsets, run_word_subsets
from solution import Solution

# %%
# Example test case
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
expected = ["facebook", "google", "leetcode"]

# %%
result = run_word_subsets(Solution, words1, words2)
result

# %%
assert_word_subsets(result, expected)
