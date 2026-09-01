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
from helpers import assert_count_stepping_numbers, run_count_stepping_numbers
from solution import Solution

# %%
# Example test case
low: int = 0
high: int = 21
expected: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]

# %%
result = run_count_stepping_numbers(Solution, low, high)
result

# %%
assert_count_stepping_numbers(result, expected)
