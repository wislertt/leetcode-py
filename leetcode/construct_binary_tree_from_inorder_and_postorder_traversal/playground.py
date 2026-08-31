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
from helpers import assert_build_tree, run_build_tree
from solution import Solution

# %%
# Example test case
inorder: list[int] = [9, 3, 15, 20, 7]
postorder: list[int] = [9, 15, 7, 20, 3]
expected_list: list[int | None] = [3, 9, 20, None, None, 15, 7]

# %%
result = run_build_tree(Solution, inorder, postorder)
result

# %%
assert_build_tree(result, expected_list)
