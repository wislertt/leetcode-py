# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_insert_into_bst, run_insert_into_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 7, 1, 3]
val = 5
expected = [1, 2, 3, 4, 5, 7]

# %%
result = run_insert_into_bst(Solution, root_list, val)
result

# %%
assert_insert_into_bst(result, expected)
