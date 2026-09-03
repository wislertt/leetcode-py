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
from helpers import assert_construct_array, run_construct_array
from solution import Solution

# %%
# Example test case
n = 3
k = 2

# %%
result = run_construct_array(Solution, n, k)
result

# %%
assert_construct_array(result, k)
