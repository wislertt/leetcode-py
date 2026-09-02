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
from helpers import assert_sum_of_left_leaves, run_sum_of_left_leaves
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected = 24

# %%
result = run_sum_of_left_leaves(Solution, root_list)
result

# %%
assert_sum_of_left_leaves(result, expected)
