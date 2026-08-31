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
from helpers import assert_longest_str_chain, run_longest_str_chain
from solution import Solution

# %%
# Example test case
words = ["a", "b", "ba", "bca", "bda", "bdca"]
expected = 4

# %%
result = run_longest_str_chain(Solution, words)
result

# %%
assert_longest_str_chain(result, expected)
