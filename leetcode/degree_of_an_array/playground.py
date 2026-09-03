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
from helpers import assert_find_shortest_sub_array, run_find_shortest_sub_array
from solution import Solution

# %%
# Example test case
nums = [1, 2, 2, 3, 1]
expected = 2

# %%
result = run_find_shortest_sub_array(Solution, nums)
result

# %%
assert_find_shortest_sub_array(result, expected)
