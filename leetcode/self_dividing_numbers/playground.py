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
from helpers import assert_self_dividing_numbers, run_self_dividing_numbers
from solution import Solution

# %%
# Example test case
left = 1
right = 22
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# %%
result = run_self_dividing_numbers(Solution, left, right)
result

# %%
assert_self_dividing_numbers(result, expected)
