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
from helpers import assert_decode_at_index, run_decode_at_index
from solution import Solution

# %%
# Example test case
s = "leet2code3"
k = 10
expected = "o"

# %%
result = run_decode_at_index(Solution, s, k)
result

# %%
assert_decode_at_index(result, expected)
