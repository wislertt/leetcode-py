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
from helpers import assert_count_prefix_suffix_pairs, run_count_prefix_suffix_pairs
from solution import Solution

# %%
# Example test case
words = ["a", "aba", "ababa", "aa"]
expected = 4

# %%
result = run_count_prefix_suffix_pairs(Solution, words)
result

# %%
assert_count_prefix_suffix_pairs(result, expected)
