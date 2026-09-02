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
from helpers import assert_min_distance, run_min_distance
from solution import Solution

# %%
# Example test case
word1 = "sea"
word2 = "eat"
expected = 2

# %%
result = run_min_distance(Solution, word1, word2)
result

# %%
assert_min_distance(result, expected)
