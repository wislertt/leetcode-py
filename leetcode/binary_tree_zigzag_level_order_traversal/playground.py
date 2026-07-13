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
from helpers import assert_zigzag_level_order, run_zigzag_level_order
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 9, 20, None, None, 15, 7]
expected = [[3], [20, 9], [15, 7]]

# %%
result = run_zigzag_level_order(Solution, root_list)
result

# %%
assert_zigzag_level_order(result, expected)
