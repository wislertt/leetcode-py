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
from helpers import assert_insert_into_max_tree, run_insert_into_max_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 1, 3, None, None, 2]
val = 5
expected_list: list[int | None] = [5, 4, None, 1, 3, None, None, 2]

# %%
result = run_insert_into_max_tree(Solution, root_list, val)
result

# %%
assert_insert_into_max_tree(result, expected_list)
