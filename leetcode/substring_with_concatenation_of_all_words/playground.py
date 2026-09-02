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
from helpers import assert_find_substring, run_find_substring
from solution import Solution

# %%
# Example test case
s = "barfoothefoobarman"
words = ["foo", "bar"]
expected = [0, 9]

# %%
result = run_find_substring(Solution, s, words)
result

# %%
assert_find_substring(result, expected)
