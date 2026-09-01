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
from helpers import assert_replace_value_in_tree, run_replace_value_in_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 4, 9, 1, 10, None, 7]
expected_list: list[int | None] = [0, 0, 0, 7, 7, None, 11]

# %%
result = run_replace_value_in_tree(Solution, root_list)
result

# %%
assert_replace_value_in_tree(result, expected_list)
