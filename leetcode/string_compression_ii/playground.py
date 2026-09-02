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
from helpers import assert_get_length_of_optimal_compression, run_get_length_of_optimal_compression
from solution import Solution

# %%
# Example test case
s = "aaabcccd"
k = 2
expected = 4

# %%
result = run_get_length_of_optimal_compression(Solution, s, k)
result

# %%
assert_get_length_of_optimal_compression(result, expected)
