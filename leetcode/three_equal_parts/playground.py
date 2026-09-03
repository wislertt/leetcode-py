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
from helpers import assert_three_equal_parts, run_three_equal_parts
from solution import Solution

# %%
# Example test case
arr = [1, 0, 1, 0, 1]
expected = [0, 3]

# %%
result = run_three_equal_parts(Solution, arr)
result

# %%
assert_three_equal_parts(result, expected)
