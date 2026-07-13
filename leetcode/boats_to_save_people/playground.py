# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_num_rescue_boats, run_num_rescue_boats
from solution import Solution

# %%
# Example test case
people = [3, 2, 2, 1]
limit = 3
expected = 3

# %%
result = run_num_rescue_boats(Solution, people, limit)
result

# %%
assert_num_rescue_boats(result, expected)
