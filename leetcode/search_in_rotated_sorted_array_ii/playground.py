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
from helpers import assert_search, run_search
from solution import Solution

# %%
# Example test case
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
expected = True

# %%
result = run_search(Solution, nums, target)
result

# %%
assert_search(result, expected)
