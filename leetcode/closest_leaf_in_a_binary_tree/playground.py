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
from helpers import assert_find_closest_leaf, run_find_closest_leaf
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4, None, None, None, 5, None, 6]
k = 2
expected = 3

# %%
result = run_find_closest_leaf(Solution, root_list, k)
result

# %%
assert_find_closest_leaf(result, expected)
