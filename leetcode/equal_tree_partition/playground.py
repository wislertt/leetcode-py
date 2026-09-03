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
from helpers import assert_check_equal_tree, run_check_equal_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 10, 10, None, None, 2, 3]
expected = True

# %%
result = run_check_equal_tree(Solution, root_list)
result

# %%
assert_check_equal_tree(result, expected)
