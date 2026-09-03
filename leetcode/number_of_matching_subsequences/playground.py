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
from helpers import assert_num_matching_subseq, run_num_matching_subseq
from solution import Solution

# %%
# Example test case
s = "abcde"
words = ["a", "bb", "acd", "ace"]
expected = 3

# %%
result = run_num_matching_subseq(Solution, s, words)
result

# %%
assert_num_matching_subseq(result, expected)
