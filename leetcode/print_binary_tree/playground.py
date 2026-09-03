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
from helpers import assert_print_tree, run_print_tree
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2]
expected = [["", "1", ""], ["2", "", ""]]

# %%
result = run_print_tree(Solution, root_list)
result

# %%
assert_print_tree(result, expected)
