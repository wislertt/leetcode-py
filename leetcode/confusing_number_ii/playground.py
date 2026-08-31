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
from helpers import assert_confusing_number_ii, run_confusing_number_ii
from solution import Solution

# %%
# Example test case
n = 20
expected = 6

# %%
result = run_confusing_number_ii(Solution, n)
result

# %%
assert_confusing_number_ii(result, expected)
