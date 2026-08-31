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
from helpers import assert_get_row, run_get_row
from solution import Solution

# %%
# Example test case
row_index: int = 3
expected: list[int] = [1, 3, 3, 1]

# %%
result = run_get_row(Solution, row_index)
result

# %%
assert_get_row(result, expected)
