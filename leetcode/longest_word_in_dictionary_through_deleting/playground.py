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
from helpers import assert_find_longest_word, run_find_longest_word
from solution import Solution

# %%
# Example test case
s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
expected = "apple"

# %%
result = run_find_longest_word(Solution, s, dictionary)
result

# %%
assert_find_longest_word(result, expected)
