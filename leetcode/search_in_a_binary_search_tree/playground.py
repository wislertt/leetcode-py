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
from helpers import assert_search_bst, run_search_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 7, 1, 3]
val = 2
expected_list: list[int | None] = [2, 1, 3]

# %%
result = run_search_bst(Solution, root_list, val)
result

# %%
assert_search_bst(result, expected_list)
