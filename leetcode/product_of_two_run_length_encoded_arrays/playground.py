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
from helpers import assert_find_rle_array, run_find_rle_array
from solution import Solution

# %%
# Example test case
encoded1 = [[1, 3], [2, 3]]
encoded2 = [[6, 3], [3, 3]]
expected = [[6, 6]]

# %%
result = run_find_rle_array(Solution, encoded1, encoded2)
result

# %%
assert_find_rle_array(result, expected)
