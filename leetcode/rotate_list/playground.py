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
from helpers import assert_rotate_right, run_rotate_right
from solution import Solution

# %%
# Example test case
head_list = [1, 2, 3, 4, 5]
k = 2
expected = [4, 5, 1, 2, 3]

# %%
result = run_rotate_right(Solution, head_list, k)
result

# %%
assert_rotate_right(result, expected)
