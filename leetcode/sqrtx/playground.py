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
from helpers import assert_my_sqrt, run_my_sqrt
from solution import Solution

# %%
# Example test case
x = 4
expected = 2

# %%
result = run_my_sqrt(Solution, x)
result

# %%
assert_my_sqrt(result, expected)
