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
from helpers import assert_champagne_tower, run_champagne_tower
from solution import Solution

# %%
# Example test case
poured = 1
query_row = 1
query_glass = 1
expected = 0.0

# %%
result = run_champagne_tower(Solution, poured, query_row, query_glass)
result

# %%
assert_champagne_tower(result, expected)
