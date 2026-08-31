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
from helpers import assert_str_str, run_str_str
from solution import Solution

# %%
# Example test case
haystack = "sadbutsad"
needle = "sad"
expected = 0

# %%
result = run_str_str(Solution, haystack, needle)
result

# %%
assert_str_str(result, expected)
