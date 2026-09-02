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
from helpers import assert_delete_node, run_delete_node
from solution import Solution

# %%
# Example test case
head_list: list[int] = [4, 5, 1, 9]
node_val = 5
expected_list = [4, 1, 9]

# %%
result = run_delete_node(Solution, head_list, node_val)
result

# %%
assert_delete_node(result, expected_list)
