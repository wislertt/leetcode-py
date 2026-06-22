# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_detect_squares, run_detect_squares
from solution import DetectSquares

# %%
# Example test case
operations = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
inputs = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
expected = [None, None, None, None, 1, 0, None, 2]

# %%
result = run_detect_squares(DetectSquares, operations, inputs)
result

# %%
assert_detect_squares(result, expected)
