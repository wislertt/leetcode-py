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
from helpers import assert_total_fruit, run_total_fruit
from solution import Solution

# %%
# Example test case
fruits = [1, 2, 3, 2, 2]
expected = 4

# %%
result = run_total_fruit(Solution, fruits)
result

# %%
assert_total_fruit(result, expected)
