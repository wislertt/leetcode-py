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
from helpers import assert_min_moves2, run_min_moves2
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3]
expected = 2

# %%
result = run_min_moves2(Solution, nums)
result

# %%
assert_min_moves2(result, expected)
