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
from helpers import assert_frequency_sort, run_frequency_sort
from solution import Solution

# %%
# Example test case
nums = [1, 1, 2, 2, 2, 3]
expected = [3, 1, 1, 2, 2, 2]

# %%
result = run_frequency_sort(Solution, nums)
result

# %%
assert_frequency_sort(result, expected)
