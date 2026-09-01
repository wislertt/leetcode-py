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
from helpers import assert_min_capability, run_min_capability
from solution import Solution

# %%
# Example test case
nums = [2, 3, 5, 9]
k = 2
expected = 5

# %%
result = run_min_capability(Solution, nums, k)
result

# %%
assert_min_capability(result, expected)
