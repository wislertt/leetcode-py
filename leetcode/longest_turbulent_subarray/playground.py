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
from helpers import assert_max_turbulence_size, run_max_turbulence_size
from solution import Solution

# %%
# Example test case
arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
expected = 5

# %%
result = run_max_turbulence_size(Solution, arr)
result

# %%
assert_max_turbulence_size(result, expected)
