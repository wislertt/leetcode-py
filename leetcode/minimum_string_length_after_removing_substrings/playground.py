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
from helpers import assert_min_length, run_min_length
from solution import Solution

# %%
# Example test case
s = "ABFCACDB"
expected = 2

# %%
result = run_min_length(Solution, s)
result

# %%
assert_min_length(result, expected)
