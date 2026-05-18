# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_merge_k_lists, run_merge_k_lists
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
lists_data = [[1, 4, 5], [1, 3, 4], [2, 6]]
expected_data = [1, 1, 2, 3, 4, 4, 5, 6]

# %%
result = run_merge_k_lists(Solution, lists_data)
ListNode[int].to_list(result) if result else []

# %%
assert_merge_k_lists(result, expected_data)
