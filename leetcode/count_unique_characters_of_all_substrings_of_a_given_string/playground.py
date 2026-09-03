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
from helpers import assert_unique_letter_string, run_unique_letter_string
from solution import Solution

# %%
# Example test case
s = "ABC"
expected = 10

# %%
result = run_unique_letter_string(Solution, s)
result

# %%
assert_unique_letter_string(result, expected)
