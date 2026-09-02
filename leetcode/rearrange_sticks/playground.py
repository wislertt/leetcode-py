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
from helpers import assert_rearrange_sticks, run_rearrange_sticks
from solution import Solution

# %%
# Example test case
n = 3
k = 2
expected = 3

# %%
result = run_rearrange_sticks(Solution, n, k)
result

# %%
assert_rearrange_sticks(result, expected)
