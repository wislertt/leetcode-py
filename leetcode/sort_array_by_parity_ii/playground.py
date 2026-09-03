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
from helpers import assert_sort_array_by_parity_ii, run_sort_array_by_parity_ii
from solution import Solution

# %%
# Example test case
nums = [4, 2, 5, 7]
expected = [4, 5, 2, 7]

# %%
result = run_sort_array_by_parity_ii(Solution, nums)
result

# %%
assert_sort_array_by_parity_ii(result, expected)
