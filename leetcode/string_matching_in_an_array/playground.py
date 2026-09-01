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
from helpers import assert_string_matching, run_string_matching
from solution import Solution

# %%
# Example test case
words = ["mass", "as", "hero", "superhero"]
expected = ["as", "hero"]

# %%
result = run_string_matching(Solution, words)
result

# %%
assert_string_matching(result, expected)
