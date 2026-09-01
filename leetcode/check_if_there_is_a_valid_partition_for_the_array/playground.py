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
from helpers import assert_valid_partition, run_valid_partition
from solution import Solution

# %%
# Example test case
nums: list[int] = [4, 4, 4, 5, 6]
expected = True

# %%
result = run_valid_partition(Solution, nums)
result

# %%
assert_valid_partition(result, expected)
