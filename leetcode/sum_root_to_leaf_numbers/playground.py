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
from helpers import assert_sum_numbers, run_sum_numbers
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [4, 9, 0, 5, 1]
expected: int = 1026

# %%
result = run_sum_numbers(Solution, root_list)
result

# %%
assert_sum_numbers(result, expected)
