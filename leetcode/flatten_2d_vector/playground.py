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
from helpers import assert_flatten_2d_vector, run_flatten_2d_vector
from solution import Vector2D

# %%
# Example test case
operations = ["Vector2D", "next", "next", "next", "has_next"]
inputs = [[[1, 2], [3], [4]], [], [], [], []]
expected = [None, 1, 2, 3, True]

# %%
result, iterator = run_flatten_2d_vector(Vector2D, operations, inputs)
print(result)
iterator

# %%
assert_flatten_2d_vector(result, expected)
