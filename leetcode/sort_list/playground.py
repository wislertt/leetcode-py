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
from helpers import assert_sort_list, run_sort_list
from solution import Solution

# %%
# Example test case
head_list = [4, 2, 1, 3]
expected = [1, 2, 3, 4]

# %%
result = run_sort_list(Solution, head_list)
result

# %%
assert_sort_list(result, expected)
