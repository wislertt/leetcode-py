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
from helpers import assert_can_partition_k_subsets, run_can_partition_k_subsets
from solution import Solution

# %%
# Example test case
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
expected = True

# %%
result = run_can_partition_k_subsets(Solution, nums, k)
result

# %%
assert_can_partition_k_subsets(result, expected)
