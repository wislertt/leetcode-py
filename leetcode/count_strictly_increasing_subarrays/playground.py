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
from helpers import assert_count_strictly_increasing, run_count_strictly_increasing
from solution import Solution

# %%
# Example test case
nums = [1, 3, 5, 4, 4, 6]
expected = 10

# %%
result = run_count_strictly_increasing(Solution, nums)
result

# %%
assert_count_strictly_increasing(result, expected)
