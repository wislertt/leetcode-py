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
from helpers import assert_height_checker, run_height_checker
from solution import Solution

# %%
# Example test case
heights = [1, 1, 4, 2, 1, 3]
expected = 3

# %%
result = run_height_checker(Solution, heights)
result

# %%
assert_height_checker(result, expected)
