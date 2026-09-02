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
from helpers import assert_lucky_numbers, run_lucky_numbers
from solution import Solution

# %%
# Example test case
matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
expected = [15]

# %%
result = run_lucky_numbers(Solution, matrix)
result

# %%
assert_lucky_numbers(result, expected)
