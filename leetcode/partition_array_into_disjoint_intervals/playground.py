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
from helpers import assert_partition_disjoint, run_partition_disjoint
from solution import Solution

# %%
# Example test case
nums = [5, 0, 3, 8, 6]
expected = 3

# %%
result = run_partition_disjoint(Solution, nums)
result

# %%
assert_partition_disjoint(result, expected)
