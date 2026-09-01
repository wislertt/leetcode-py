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
from helpers import assert_maximize_sweetness, run_maximize_sweetness
from solution import Solution

# %%
# Example test case
sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5
expected = 6

# %%
result = run_maximize_sweetness(Solution, sweetness, k)
result

# %%
assert_maximize_sweetness(result, expected)
