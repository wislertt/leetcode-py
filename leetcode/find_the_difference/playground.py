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
from helpers import assert_find_the_difference, run_find_the_difference
from solution import Solution

# %%
# Example test case
s = "abcd"
t = "abcde"
expected = "e"

# %%
result = run_find_the_difference(Solution, s, t)
result

# %%
assert_find_the_difference(result, expected)
