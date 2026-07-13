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
from helpers import assert_inorder_successor, run_inorder_successor
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 1, 3]
p_val = 1
expected_val = 2

# %%
result = run_inorder_successor(Solution, root_list, p_val)
result

# %%
assert_inorder_successor(result, expected_val)
