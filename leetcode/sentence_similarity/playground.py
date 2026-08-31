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
from helpers import assert_are_sentences_similar, run_are_sentences_similar
from solution import Solution

# %%
# Example test case
sentence1 = ["great", "acting", "skills"]
sentence2 = ["fine", "drama", "talent"]
similar_pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
expected = True

# %%
result = run_are_sentences_similar(Solution, sentence1, sentence2, similar_pairs)
result

# %%
assert_are_sentences_similar(result, expected)
