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
from helpers import assert_max_frequency, run_max_frequency
from solution import Solution

# %%
# Example test case
nums = [1, 2, 3, 4, 5, 6]
k = 1
expected = 2

# %%
result = run_max_frequency(Solution, nums, k)
result

# %%
assert_max_frequency(result, expected)
