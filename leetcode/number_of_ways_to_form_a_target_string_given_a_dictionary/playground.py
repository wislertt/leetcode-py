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
from helpers import assert_num_ways, run_num_ways
from solution import Solution

# %%
# Example test case
words = ["acca", "bbbb", "caca"]
target = "aba"
expected = 6

# %%
result = run_num_ways(Solution, words, target)
result

# %%
assert_num_ways(result, expected)
