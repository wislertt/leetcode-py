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
from helpers import assert_delete_duplicates_unsorted, run_delete_duplicates_unsorted
from solution import Solution

from leetcode_py import ListNode

# %%
# Example test case
head_vals = [1, 2, 3, 2]
expected_vals = [1, 3]

# %%
result = run_delete_duplicates_unsorted(Solution, head_vals)
ListNode[int].to_list(result) if result else []

# %%
assert_delete_duplicates_unsorted(result, expected_vals)
