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
from helpers import assert_number_of_arrays, run_number_of_arrays
from solution import Solution

# %%
# Example test case
differences = [1, -3, 4]
lower = 1
upper = 6
expected = 2

# %%
result = run_number_of_arrays(Solution, differences, lower, upper)
result

# %%
assert_number_of_arrays(result, expected)
