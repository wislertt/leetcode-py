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
from helpers import assert_insertion_sort_list, run_insertion_sort_list
from solution import Solution

# %%
# Example test case
head_vals: list[int] = [4, 2, 1, 3]
expected_vals: list[int] = [1, 2, 3, 4]

# %%
result = run_insertion_sort_list(Solution, head_vals)
result

# %%
assert_insertion_sort_list(result, expected_vals)
