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
from helpers import assert_split_bst, run_split_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 6, 1, 3, 5, 7]
target = 2
expected_lists: list[list[int | None]] = [[2, 1], [4, 3, 6, None, None, 5, 7]]

# %%
result = run_split_bst(Solution, root_list, target)
result

# %%
assert_split_bst(result, expected_lists)
