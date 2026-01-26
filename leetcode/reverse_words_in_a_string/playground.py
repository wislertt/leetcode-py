# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_reverse_words, run_reverse_words
from solution import Solution

# %%
# Example test case
s: str = "the sky is blue"
expected: str = "blue is sky the"

# %%
result = run_reverse_words(Solution, s)
print(f"Reversed words: {result}")
result

# %%
assert_reverse_words(result, expected)
