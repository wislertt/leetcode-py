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
from helpers import assert_maximum_swap, run_maximum_swap
from solution import Solution

# %%
# Example test case
num = 2736
expected = 7236

# %%
result = run_maximum_swap(Solution, num)
result

# %%
assert_maximum_swap(result, expected)
