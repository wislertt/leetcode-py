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
from helpers import assert_find_permutation, run_find_permutation
from solution import Solution

# %%
# Example test case
s = "DI"
expected = [2, 1, 3]

# %%
result = run_find_permutation(Solution, s)
result

# %%
assert_find_permutation(result, expected)
