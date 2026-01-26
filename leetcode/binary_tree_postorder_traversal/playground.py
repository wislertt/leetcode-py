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
from helpers import assert_postorder_traversal, run_postorder_traversal
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, None, 2, 3]
expected: list[int] = [3, 2, 1]

# %%
result = run_postorder_traversal(Solution, root_list)
print(f"Postorder traversal: {result}")
result

# %%
assert_postorder_traversal(result, expected)
