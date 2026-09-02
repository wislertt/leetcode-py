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
from helpers import assert_repeated_substring_pattern, run_repeated_substring_pattern
from solution import Solution

# %%
# Example test case
s = "abab"
expected = True

# %%
result = run_repeated_substring_pattern(Solution, s)
result

# %%
assert_repeated_substring_pattern(result, expected)
