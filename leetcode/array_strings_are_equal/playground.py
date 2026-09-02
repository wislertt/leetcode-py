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
from helpers import assert_array_strings_are_equal, run_array_strings_are_equal
from solution import Solution

# %%
# Example test case
word1 = ["ab", "c"]
word2 = ["a", "bc"]
expected = True

# %%
result = run_array_strings_are_equal(Solution, word1, word2)
result

# %%
assert_array_strings_are_equal(result, expected)
