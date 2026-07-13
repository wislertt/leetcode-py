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
from helpers import assert_random_pick_operations, run_random_pick_operations
from solution import Solution

# %%
# Example test case - single element, deterministic output
operations = ["Solution", "pickIndex"]
inputs = [[1], []]
expected = [None, 0]

# %%
result = run_random_pick_operations(Solution, operations, inputs)
result

# %%
assert_random_pick_operations(result, expected)
