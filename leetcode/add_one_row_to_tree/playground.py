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
from helpers import assert_add_one_row, run_add_one_row
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 2, 6, 3, 1, 5]
val = 1
depth = 2
expected_list: list[int | None] = [4, 1, 1, 2, None, None, 6, 3, 1, 5]

# %%
result = run_add_one_row(Solution, root_list, val, depth)
result

# %%
assert_add_one_row(result, expected_list)
