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
from helpers import assert_min_height_shelves, run_min_height_shelves
from solution import Solution

# %%
# Example test case
books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelf_width = 4
expected = 6

# %%
result = run_min_height_shelves(Solution, books, shelf_width)
result

# %%
assert_min_height_shelves(result, expected)
