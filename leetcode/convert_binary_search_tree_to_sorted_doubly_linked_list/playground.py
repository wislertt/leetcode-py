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
from helpers import assert_tree_to_doubly_list, run_tree_to_doubly_list
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 5, 1, 3]
expected_list = [1, 2, 3, 4, 5]

# %%
result = run_tree_to_doubly_list(Solution, root_list)
result

# %%
assert_tree_to_doubly_list(result, expected_list)
