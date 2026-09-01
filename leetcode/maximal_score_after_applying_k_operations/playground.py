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
from helpers import assert_max_kelements, run_max_kelements
from solution import Solution

# %%
# Example test case
nums = [1, 10, 3, 3, 3]
k = 3
expected = 17

# %%
result = run_max_kelements(Solution, nums, k)
result

# %%
assert_max_kelements(result, expected)
