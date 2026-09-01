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
from helpers import assert_number_of_ways, run_number_of_ways
from solution import Solution

# %%
# Example test case
num_people = 4
expected = 2

# %%
result = run_number_of_ways(Solution, num_people)
result

# %%
assert_number_of_ways(result, expected)
