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
from helpers import assert_full_bloom_flowers, run_full_bloom_flowers
from solution import Solution

# %%
# Example test case
flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
people = [2, 3, 7, 11]
expected = [1, 2, 2, 2]

# %%
result = run_full_bloom_flowers(Solution, flowers, people)
result

# %%
assert_full_bloom_flowers(result, expected)
