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
from helpers import assert_kth_largest, run_kth_largest
from solution import KthLargest

# %%
# Example test case
operations = ["KthLargest", "add", "add", "add", "add", "add"]
inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
expected = [None, 4, 5, 5, 8, 8]

# %%
result = run_kth_largest(KthLargest, operations, inputs)
result

# %%
assert_kth_largest(result, expected)
