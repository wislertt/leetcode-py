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
from helpers import assert_binary_tree_paths, run_binary_tree_paths
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, None, 5]
expected: list[str] = ["1->2->5", "1->3"]

# %%
result = run_binary_tree_paths(Solution, root_list)
result

# %%
assert_binary_tree_paths(result, expected)
