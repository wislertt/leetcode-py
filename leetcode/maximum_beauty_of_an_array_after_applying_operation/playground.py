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
from helpers import assert_maximum_beauty, run_maximum_beauty
from solution import Solution

# %%
# Example test case
nums = [4, 6, 1, 2]
k = 2
expected = 3

# %%
result = run_maximum_beauty(Solution, nums, k)
result

# %%
assert_maximum_beauty(result, expected)
