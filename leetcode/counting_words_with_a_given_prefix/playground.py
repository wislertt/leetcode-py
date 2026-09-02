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
from helpers import assert_prefix_count, run_prefix_count
from solution import Solution

# %%
# Example test case
words = ["pay", "attention", "practice", "attend"]
pref = "at"
expected = 2

# %%
result = run_prefix_count(Solution, words, pref)
result

# %%
assert_prefix_count(result, expected)
