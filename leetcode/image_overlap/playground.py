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
from helpers import assert_largest_overlap, run_largest_overlap
from solution import Solution

# %%
# Example test case
img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
expected = 3

# %%
result = run_largest_overlap(Solution, img1, img2)
result

# %%
assert_largest_overlap(result, expected)
