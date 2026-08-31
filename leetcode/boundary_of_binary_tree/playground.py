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
from helpers import assert_boundary_of_binary_tree, run_boundary_of_binary_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, None, 2, 3, 4]
expected = [1, 3, 4, 2]

# %%
result = run_boundary_of_binary_tree(Solution, root_list)
result

# %%
assert_boundary_of_binary_tree(result, expected)
