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
from helpers import assert_find_bottom_left_value, run_find_bottom_left_value
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [2, 1, 3]
expected = 1

# %%
result = run_find_bottom_left_value(Solution, root_list)
result

# %%
assert_find_bottom_left_value(result, expected)
