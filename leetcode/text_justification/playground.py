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
from helpers import assert_full_justify, run_full_justify
from solution import Solution

# %%
# Example test case
words = ["This", "is", "an", "example", "of", "text", "justification."]
max_width = 16
expected = ["This    is    an", "example  of text", "justification.  "]

# %%
result = run_full_justify(Solution, words, max_width)
result

# %%
assert_full_justify(result, expected)
