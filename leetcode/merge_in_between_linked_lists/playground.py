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
from helpers import assert_merge_in_between, run_merge_in_between
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
list1_vals = [10, 1, 13, 6, 9, 5]
a = 3
b = 4
list2_vals = [1000000, 1000001, 1000002]
expected_vals = [10, 1, 13, 1000000, 1000001, 1000002, 5]

# %%
result = run_merge_in_between(Solution, list1_vals, a, b, list2_vals)
ListNode[int].to_list(result) if result else []

# %%
assert_merge_in_between(result, expected_vals)
