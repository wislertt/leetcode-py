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
from helpers import assert_lexicographically_smallest_array, run_lexicographically_smallest_array
from solution import Solution

# %%
# Example test case
nums = [1, 5, 3, 9, 8]
limit = 2
expected = [1, 3, 5, 8, 9]

# %%
result = run_lexicographically_smallest_array(Solution, nums, limit)
result

# %%
assert_lexicographically_smallest_array(result, expected)
