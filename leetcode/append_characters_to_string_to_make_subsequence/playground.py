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
from helpers import assert_append_characters, run_append_characters
from solution import Solution

# %%
# Example test case
s = "coaching"
t = "coding"
expected = 4

# %%
result = run_append_characters(Solution, s, t)
result

# %%
assert_append_characters(result, expected)
