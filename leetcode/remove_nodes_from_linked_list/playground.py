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
from helpers import assert_remove_nodes, run_remove_nodes
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
head_vals: list[int] = [5, 2, 13, 3, 8]
expected_vals: list[int] = [13, 8]

# %%
result = run_remove_nodes(Solution, head_vals)
ListNode[int].to_list(result) if result else []

# %%
assert_remove_nodes(result, expected_vals)
