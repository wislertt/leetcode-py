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
from helpers import assert_remove_duplicates, run_remove_duplicates
from solution import Solution

# %%
# Example test case
s = "deeedbbcccbdaa"
k = 3
expected = "aa"

# %%
result = run_remove_duplicates(Solution, s, k)
result

# %%
assert_remove_duplicates(result, expected)
