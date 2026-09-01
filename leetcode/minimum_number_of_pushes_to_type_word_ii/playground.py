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
from helpers import assert_minimum_pushes, run_minimum_pushes
from solution import Solution

# %%
# Example test case
word = "abcde"
expected = 5

# %%
result = run_minimum_pushes(Solution, word)
result

# %%
assert_minimum_pushes(result, expected)
