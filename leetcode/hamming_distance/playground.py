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
from helpers import assert_hamming_distance, run_hamming_distance
from solution import Solution

# %%
# Example test case
x = 1
y = 4
expected = 2

# %%
result = run_hamming_distance(Solution, x, y)
result

# %%
assert_hamming_distance(result, expected)
