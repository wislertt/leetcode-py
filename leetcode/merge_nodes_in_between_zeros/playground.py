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
from helpers import assert_merge_nodes, run_merge_nodes
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
head_vals: list[int] = [0, 3, 1, 0, 4, 5, 2, 0]
expected_vals: list[int] = [4, 11]

# %%
result = run_merge_nodes(Solution, head_vals)
ListNode[int].to_list(result) if result else []

# %%
assert_merge_nodes(result, expected_vals)
