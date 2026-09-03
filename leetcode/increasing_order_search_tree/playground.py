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
from helpers import assert_increasing_bst, run_increasing_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
expected_list: list[int | None] = [
    1,
    None,
    2,
    None,
    3,
    None,
    4,
    None,
    5,
    None,
    6,
    None,
    7,
    None,
    8,
    None,
    9,
]

# %%
result = run_increasing_bst(Solution, root_list)
result

# %%
assert_increasing_bst(result, expected_list)
