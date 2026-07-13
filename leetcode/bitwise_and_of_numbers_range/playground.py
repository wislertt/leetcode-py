# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_range_bitwise_and, run_range_bitwise_and
from solution import Solution

# %%
# Example test case
left = 5
right = 7
expected = 4

# %%
result = run_range_bitwise_and(Solution, left, right)
result

# %%
assert_range_bitwise_and(result, expected)
