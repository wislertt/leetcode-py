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
from helpers import assert_is_even_odd_tree, run_is_even_odd_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
expected = True

# %%
result = run_is_even_odd_tree(Solution, root_list)
result

# %%
assert_is_even_odd_tree(result, expected)
