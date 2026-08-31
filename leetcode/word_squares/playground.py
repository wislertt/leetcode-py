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
from helpers import assert_word_squares, run_word_squares
from solution import Solution

# %%
# Example test case
words = ["area", "lead", "wall", "lady", "ball"]
expected = [["ball", "area", "lead", "lady"], ["wall", "area", "lead", "lady"]]

# %%
result = run_word_squares(Solution, words)
result

# %%
assert_word_squares(result, expected)
