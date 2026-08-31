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
from helpers import assert_upside_down_binary_tree, run_upside_down_binary_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4, 5]
expected_list: list[int | None] = [4, 5, 2, None, None, 3, 1]

# %%
result = run_upside_down_binary_tree(Solution, root_list)
result

# %%
assert_upside_down_binary_tree(result, expected_list)
