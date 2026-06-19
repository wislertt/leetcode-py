# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_plus_one, run_plus_one
from solution import Solution

# %%
# Example test case
digits = [1, 2, 3]
expected = [1, 2, 4]

# %%
result = run_plus_one(Solution, digits)
result

# %%
assert_plus_one(result, expected)
