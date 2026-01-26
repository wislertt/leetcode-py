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
from helpers import assert_preorder_traversal, run_preorder_traversal
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, None, 2, 3]
expected: list[int] = [1, 2, 3]

# %%
result = run_preorder_traversal(Solution, root_list)
print(f"Preorder traversal: {result}")
result

# %%
assert_preorder_traversal(result, expected)
