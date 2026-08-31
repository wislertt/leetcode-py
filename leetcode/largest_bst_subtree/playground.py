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
from helpers import assert_largest_bst_subtree, run_largest_bst_subtree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [10, 5, 15, 1, 8, None, 7]
expected = 3

# %%
result = run_largest_bst_subtree(Solution, root_list)
result

# %%
assert_largest_bst_subtree(result, expected)
