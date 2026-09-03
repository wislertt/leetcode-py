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
from helpers import assert_find_black_pixel, run_find_black_pixel
from solution import Solution

# %%
# Example test case
picture = [["W", "B", "W"], ["W", "B", "W"], ["W", "B", "W"]]
target = 1
expected = 0

# %%
result = run_find_black_pixel(Solution, picture, target)
result

# %%
assert_find_black_pixel(result, expected)
