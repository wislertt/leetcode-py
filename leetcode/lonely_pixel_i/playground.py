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
from helpers import assert_find_lonely_pixel, run_find_lonely_pixel
from solution import Solution

# %%
# Example test case
picture = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]
expected = 3

# %%
result = run_find_lonely_pixel(Solution, picture)
result

# %%
assert_find_lonely_pixel(result, expected)
