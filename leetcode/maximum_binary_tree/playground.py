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
from helpers import assert_construct_maximum_binary_tree, run_construct_maximum_binary_tree
from solution import Solution

# %%
# Example test case
nums: list[int] = [3, 2, 1, 6, 0, 5]
expected_list: list[int | None] = [6, 3, 5, None, 2, 0, None, None, 1]

# %%
result = run_construct_maximum_binary_tree(Solution, nums)
result

# %%
assert_construct_maximum_binary_tree(result, expected_list)
