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
from helpers import assert_num_ways, run_num_ways
from solution import Solution

# %%
# Example test case
steps = 3
arr_len = 2
expected = 4

# %%
result = run_num_ways(Solution, steps, arr_len)
result

# %%
assert_num_ways(result, expected)
