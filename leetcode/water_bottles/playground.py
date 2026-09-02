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
from helpers import assert_num_water_bottles, run_num_water_bottles
from solution import Solution

# %%
# Example test case
num_bottles = 9
num_exchange = 3
expected = 13

# %%
result = run_num_water_bottles(Solution, num_bottles, num_exchange)
result

# %%
assert_num_water_bottles(result, expected)
