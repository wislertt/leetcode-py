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
from helpers import assert_count_letters, run_count_letters
from solution import Solution

# %%
# Example test case
s = "aaaba"
expected = 8

# %%
result = run_count_letters(Solution, s)
result

# %%
assert_count_letters(result, expected)
