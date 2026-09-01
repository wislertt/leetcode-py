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
from helpers import assert_get_happy_string, run_get_happy_string
from solution import Solution

# %%
# Example test case
n = 3
k = 9
expected = "cab"

# %%
result = run_get_happy_string(Solution, n, k)
result

# %%
assert_get_happy_string(result, expected)
