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
from helpers import assert_max_sum_after_partitioning, run_max_sum_after_partitioning
from solution import Solution

# %%
# Example test case
arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
expected = 84

# %%
result = run_max_sum_after_partitioning(Solution, arr, k)
result

# %%
assert_max_sum_after_partitioning(result, expected)
