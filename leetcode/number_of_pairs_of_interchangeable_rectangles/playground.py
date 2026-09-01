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
from helpers import assert_interchangeable_rectangles, run_interchangeable_rectangles
from solution import Solution

# %%
# Example test case
rectangles: list[list[int]] = [[4, 8], [3, 6], [10, 20], [15, 30]]
expected = 6

# %%
result = run_interchangeable_rectangles(Solution, rectangles)
result

# %%
assert_interchangeable_rectangles(result, expected)
