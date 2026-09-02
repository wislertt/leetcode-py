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
from helpers import assert_count_of_substrings, run_count_of_substrings
from solution import Solution

# %%
# Example test case
word = "ieaouqqieaouqq"
k = 1
expected = 3

# %%
result = run_count_of_substrings(Solution, word, k)
result

# %%
assert_count_of_substrings(result, expected)
