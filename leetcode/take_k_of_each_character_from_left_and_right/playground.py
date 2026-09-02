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
from helpers import assert_take_characters, run_take_characters
from solution import Solution

# %%
# Example test case
s = "aabaaaacaabc"
k = 2
expected = 8

# %%
result = run_take_characters(Solution, s, k)
result

# %%
assert_take_characters(result, expected)
