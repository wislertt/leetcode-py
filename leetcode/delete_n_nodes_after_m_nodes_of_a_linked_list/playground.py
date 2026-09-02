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
from helpers import assert_delete_nodes, run_delete_nodes
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
head_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
m = 2
n = 3
expected_vals = [1, 2, 6, 7, 11, 12]

# %%
result = run_delete_nodes(Solution, head_vals, m, n)
ListNode[int].to_list(result) if result else []

# %%
assert_delete_nodes(result, expected_vals)
