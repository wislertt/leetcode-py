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
from helpers import assert_smallest_common_element, run_smallest_common_element
from solution import Solution

# %%
# Example test case
mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
expected = 5

# %%
result = run_smallest_common_element(Solution, mat)
result

# %%
assert_smallest_common_element(result, expected)
