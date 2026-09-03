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
from helpers import assert_prune_tree, run_prune_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, None, 0, 0, 1]
expected_list: list[int | None] = [1, None, 0, None, 1]

# %%
result = run_prune_tree(Solution, root_list)
result

# %%
assert_prune_tree(result, expected_list)
