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
from helpers import assert_count_vowel_permutation, run_count_vowel_permutation
from solution import Solution

# %%
# Example test case
n = 5
expected = 68

# %%
result = run_count_vowel_permutation(Solution, n)
result

# %%
assert_count_vowel_permutation(result, expected)
