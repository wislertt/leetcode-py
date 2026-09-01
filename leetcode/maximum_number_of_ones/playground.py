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
from helpers import assert_maximum_number_of_ones, run_maximum_number_of_ones
from solution import Solution

# %%
# Example test case
width = 3
height = 3
side_length = 2
max_ones = 1
expected = 4

# %%
result = run_maximum_number_of_ones(Solution, width, height, side_length, max_ones)
result

# %%
assert_maximum_number_of_ones(result, expected)
