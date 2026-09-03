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
from helpers import assert_find_and_replace_pattern, run_find_and_replace_pattern
from solution import Solution

# %%
# Example test case
words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"
expected = ["mee", "aqq"]

# %%
result = run_find_and_replace_pattern(Solution, words, pattern)
result

# %%
assert_find_and_replace_pattern(result, expected)
