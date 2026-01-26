# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_inorder_traversal, run_inorder_traversal
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, None, 2, None, None, 3]
expected = [1, 3, 2]

# %%
result = run_inorder_traversal(Solution, root_list)
result

# %%
assert_inorder_traversal(result, expected)
