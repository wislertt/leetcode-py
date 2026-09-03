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
from helpers import assert_letter_case_permutation, run_letter_case_permutation
from solution import Solution

# %%
# Example test case
s = "a1b2"
expected = ["a1b2", "a1B2", "A1b2", "A1B2"]

# %%
result = run_letter_case_permutation(Solution, s)
result

# %%
assert_letter_case_permutation(result, expected)
