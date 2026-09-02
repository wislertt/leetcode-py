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
from helpers import assert_construct_rectangle, run_construct_rectangle
from solution import Solution

# %%
# Example test case
area = 4
expected = [2, 2]

# %%
result = run_construct_rectangle(Solution, area)
result

# %%
assert_construct_rectangle(result, expected)
