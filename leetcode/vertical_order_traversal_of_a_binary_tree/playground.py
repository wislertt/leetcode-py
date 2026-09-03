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
from helpers import assert_vertical_traversal, run_vertical_traversal
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected_list: list[list[int]] = [[9], [3, 15], [20], [7]]

# %%
result = run_vertical_traversal(Solution, root_list)
result

# %%
assert_vertical_traversal(result, expected_list)
