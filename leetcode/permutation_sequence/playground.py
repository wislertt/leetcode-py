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
from helpers import assert_get_permutation, run_get_permutation
from solution import Solution

# %%
# Example test case
n = 3
k = 3
expected = "213"

# %%
result = run_get_permutation(Solution, n, k)
result

# %%
assert_get_permutation(result, expected)
