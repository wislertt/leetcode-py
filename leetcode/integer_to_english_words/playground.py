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
from helpers import assert_number_to_words, run_number_to_words
from solution import Solution

# %%
# Example test case
num = 1234567
expected = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# %%
result = run_number_to_words(Solution, num)
result

# %%
assert_number_to_words(result, expected)
