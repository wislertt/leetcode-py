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
from helpers import assert_image_smoother, run_image_smoother
from solution import Solution

# %%
# Example test case
img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# %%
result = run_image_smoother(Solution, img)
result

# %%
assert_image_smoother(result, expected)
