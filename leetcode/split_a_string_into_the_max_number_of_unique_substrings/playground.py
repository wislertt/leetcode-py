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
from helpers import assert_max_unique_split, run_max_unique_split
from solution import Solution

# %%
# Example test case
s = "ababccc"
expected = 5

# %%
result = run_max_unique_split(Solution, s)
result

# %%
assert_max_unique_split(result, expected)
