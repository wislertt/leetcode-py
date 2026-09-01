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
from helpers import assert_max_boxes_in_warehouse, run_max_boxes_in_warehouse
from solution import Solution

# %%
# Example test case
boxes = [4, 3, 4, 1]
warehouse = [5, 3, 3, 4, 1]
expected = 3

# %%
result = run_max_boxes_in_warehouse(Solution, boxes, warehouse)
result

# %%
assert_max_boxes_in_warehouse(result, expected)
