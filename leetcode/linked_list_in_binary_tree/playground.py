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
from helpers import assert_is_sub_path, run_is_sub_path
from solution import Solution

# %%
# Example test case
head_list: list[int] = [4, 2, 8]
root_list: list[int | None] = [
    1,
    4,
    4,
    None,
    2,
    2,
    None,
    1,
    None,
    6,
    8,
    None,
    None,
    None,
    None,
    1,
    3,
]
expected = True

# %%
result = run_is_sub_path(Solution, head_list, root_list)
result

# %%
assert_is_sub_path(result, expected)
