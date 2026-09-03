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
from helpers import assert_minimum_length_encoding, run_minimum_length_encoding
from solution import Solution

# %%
# Example test case
words = ["time", "me", "bell"]
expected = 10

# %%
result = run_minimum_length_encoding(Solution, words)
result

# %%
assert_minimum_length_encoding(result, expected)
