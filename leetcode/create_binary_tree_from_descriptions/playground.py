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
from helpers import assert_create_binary_tree, run_create_binary_tree
from solution import Solution

# %%
# Example test case
descriptions_list: list[list[int]] = [
    [20, 15, 1],
    [20, 17, 0],
    [50, 20, 1],
    [50, 80, 0],
    [80, 19, 1],
]
expected_list: list[int | None] = [50, 20, 80, 15, 17, 19]

# %%
result = run_create_binary_tree(Solution, descriptions_list)
result

# %%
assert_create_binary_tree(result, expected_list)
