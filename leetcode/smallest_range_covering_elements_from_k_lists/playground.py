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
from helpers import assert_smallest_range, run_smallest_range
from solution import Solution

# %%
# Example test case
nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
expected = [20, 24]

# %%
result = run_smallest_range(Solution, nums)
result

# %%
assert_smallest_range(result, expected)
