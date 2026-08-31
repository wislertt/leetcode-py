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
from helpers import assert_partition, run_partition
from solution import Solution

# %%
# Example test case
head_list = [1, 4, 3, 2, 5, 2]
x = 3
expected_list = [1, 2, 2, 4, 3, 5]

# %%
result = run_partition(Solution, head_list, x)
result

# %%
assert_partition(result, expected_list)
