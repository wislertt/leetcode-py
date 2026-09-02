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
from helpers import assert_flatten, run_flatten
from solution import Solution

# %%
# Example test case
head_list: list[int | None] = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
expected_list: list[int | None] = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

# %%
result = run_flatten(Solution, head_list)
result

# %%
assert_flatten(result, expected_list)
