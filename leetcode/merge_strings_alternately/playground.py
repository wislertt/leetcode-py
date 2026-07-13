# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_merge_alternately, run_merge_alternately
from solution import Solution

# %%
# Example test case
word1 = "abc"
word2 = "pqr"
expected = "apbqcr"

# %%
result = run_merge_alternately(Solution, word1, word2)
result

# %%
assert_merge_alternately(result, expected)
