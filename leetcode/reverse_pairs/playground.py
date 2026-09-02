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
from helpers import assert_reverse_pairs, run_reverse_pairs
from solution import Solution

# %%
# Example test case
nums = [1, 3, 2, 3, 1]
expected = 2

# %%
result = run_reverse_pairs(Solution, nums)
result

# %%
assert_reverse_pairs(result, expected)
