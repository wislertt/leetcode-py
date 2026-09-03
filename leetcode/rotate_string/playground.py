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
from helpers import assert_rotate_string, run_rotate_string
from solution import Solution

# %%
# Example test case
s = "abcde"
goal = "cdeab"
expected = True

# %%
result = run_rotate_string(Solution, s, goal)
result

# %%
assert_rotate_string(result, expected)
