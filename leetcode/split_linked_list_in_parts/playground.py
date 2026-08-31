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
from helpers import assert_split_list_to_parts, run_split_list_to_parts
from solution import Solution

# %%
# Example test case
head_vals: list[int] = [1, 2, 3]
k = 5
expected = [[1], [2], [3], [], []]

# %%
result = run_split_list_to_parts(Solution, head_vals, k)
result

# %%
assert_split_list_to_parts(result, expected)
