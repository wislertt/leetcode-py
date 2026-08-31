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
from helpers import assert_k_inverse_pairs, run_k_inverse_pairs
from solution import Solution

# %%
# Example test case
n = 3
k = 1
expected = 2

# %%
result = run_k_inverse_pairs(Solution, n, k)
result

# %%
assert_k_inverse_pairs(result, expected)
