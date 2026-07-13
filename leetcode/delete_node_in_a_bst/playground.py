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
from helpers import assert_delete_node, run_delete_node
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 3, 6, 2, 4, None, 7]
key = 3
expected = [2, 4, 5, 6, 7]

# %%
result = run_delete_node(Solution, root_list, key)
result

# %%
assert_delete_node(result, expected)
