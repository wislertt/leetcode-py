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
from helpers import assert_minimum_operations, run_minimum_operations
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
expected = 3

# %%
result = run_minimum_operations(Solution, root_list)
result

# %%
assert_minimum_operations(result, expected)
