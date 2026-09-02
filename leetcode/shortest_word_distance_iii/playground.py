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
from helpers import assert_shortest_word_distance_iii, run_shortest_word_distance_iii
from solution import Solution

# %%
# Example test case
words_dict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
expected = 3

# %%
result = run_shortest_word_distance_iii(Solution, words_dict, word1, word2)
result

# %%
assert_shortest_word_distance_iii(result, expected)
