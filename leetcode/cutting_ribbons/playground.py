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
from helpers import assert_max_length, run_max_length
from solution import Solution

# %%
# Example test case
ribbons = [9, 7, 5]
k = 3
expected = 5

# %%
result = run_max_length(Solution, ribbons, k)
result

# %%
assert_max_length(result, expected)
