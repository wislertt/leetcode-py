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
from helpers import assert_reach_number, run_reach_number
from solution import Solution

# %%
# Example test case
target = 2
expected = 3

# %%
result = run_reach_number(Solution, target)
result

# %%
assert_reach_number(result, expected)
