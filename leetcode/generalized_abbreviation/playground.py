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
from helpers import assert_generate_abbreviations, run_generate_abbreviations
from solution import Solution

# %%
# Example test case
word = "word"
expected = [
    "4",
    "3d",
    "2r1",
    "2rd",
    "1o2",
    "1o1d",
    "1or1",
    "1ord",
    "w3",
    "w2d",
    "w1r1",
    "w1rd",
    "wo2",
    "wo1d",
    "wor1",
    "word",
]

# %%
result = run_generate_abbreviations(Solution, word)
result

# %%
assert_generate_abbreviations(result, expected)
