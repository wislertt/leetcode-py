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
from helpers import assert_reverse_vowels, run_reverse_vowels
from solution import Solution

# %%
# Example test case
s = "IceCreAm"
expected = "AceCreIm"

# %%
result = run_reverse_vowels(Solution, s)
result

# %%
assert_reverse_vowels(result, expected)
