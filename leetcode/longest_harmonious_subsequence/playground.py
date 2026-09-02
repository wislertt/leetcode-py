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
from helpers import assert_find_lhs, run_find_lhs
from solution import Solution

# %%
# Example test case
nums: list[int] = [1, 3, 2, 2, 5, 2, 3, 7]
expected = 5

# %%
result = run_find_lhs(Solution, nums)
result

# %%
assert_find_lhs(result, expected)
