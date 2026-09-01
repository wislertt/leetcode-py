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
from helpers import assert_make_equal, run_make_equal
from solution import Solution

# %%
# Example test case
words: list[str] = ["abc", "aabc", "bc"]
expected = True

# %%
result = run_make_equal(Solution, words)
result

# %%
assert_make_equal(result, expected)
