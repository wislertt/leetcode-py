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
from helpers import assert_min_area, run_min_area
from solution import Solution

# %%
# Example test case
image = [["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]]
x = 0
y = 2
expected = 6

# %%
result = run_min_area(Solution, image, x, y)
result

# %%
assert_min_area(result, expected)
