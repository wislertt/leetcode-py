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
from helpers import assert_convert_bst, run_convert_bst
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
expected_list: list[int | None] = [
    30,
    36,
    21,
    36,
    35,
    26,
    15,
    None,
    None,
    None,
    33,
    None,
    None,
    None,
    8,
]

# %%
result = run_convert_bst(Solution, root_list)
result

# %%
assert_convert_bst(result, expected_list)
