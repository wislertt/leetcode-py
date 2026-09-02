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
from helpers import assert_add_spaces, run_add_spaces
from solution import Solution

# %%
# Example test case
s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]
expected = "Leetcode Helps Me Learn"

# %%
result = run_add_spaces(Solution, s, spaces)
result

# %%
assert_add_spaces(result, expected)
