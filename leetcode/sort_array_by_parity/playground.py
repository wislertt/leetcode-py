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
from helpers import assert_sort_array_by_parity, run_sort_array_by_parity
from solution import Solution

# %%
# Example test case
nums = [3, 1, 2, 4]
expected = [2, 4, 3, 1]

# %%
result = run_sort_array_by_parity(Solution, nums)
result

# %%
assert_sort_array_by_parity(result, expected)
