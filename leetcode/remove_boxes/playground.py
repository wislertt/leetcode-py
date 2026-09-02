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
from helpers import assert_remove_boxes, run_remove_boxes
from solution import Solution

# %%
# Example test case
boxes: list[int] = [1, 3, 2, 2, 2, 3, 4, 3, 1]
expected = 23

# %%
result = run_remove_boxes(Solution, boxes)
result

# %%
assert_remove_boxes(result, expected)
