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
from helpers import assert_get_factors, run_get_factors
from solution import Solution

# %%
# Example test case
n = 12
expected = [[2, 6], [3, 4], [2, 2, 3]]

# %%
result = run_get_factors(Solution, n)
result

# %%
assert_get_factors(result, expected)
