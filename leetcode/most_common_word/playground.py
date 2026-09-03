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
from helpers import assert_most_common_word, run_most_common_word
from solution import Solution

# %%
# Example test case
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
expected = "ball"

# %%
result = run_most_common_word(Solution, paragraph, banned)
result

# %%
assert_most_common_word(result, expected)
