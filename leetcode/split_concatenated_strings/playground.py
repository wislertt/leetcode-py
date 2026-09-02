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
from helpers import assert_split_looping_string, run_split_looping_string
from solution import Solution

# %%
# Example test case
strs = ["abc", "xyz"]
expected = "zyxcba"

# %%
result = run_split_looping_string(Solution, strs)
result

# %%
assert_split_looping_string(result, expected)
