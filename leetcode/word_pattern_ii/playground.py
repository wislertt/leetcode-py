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
from helpers import assert_word_pattern_match, run_word_pattern_match
from solution import Solution

# %%
# Example test case
pattern = "abab"
s = "redblueredblue"
expected = True

# %%
result = run_word_pattern_match(Solution, pattern, s)
result

# %%
assert_word_pattern_match(result, expected)
