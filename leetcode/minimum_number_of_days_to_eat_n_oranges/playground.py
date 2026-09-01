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
from helpers import assert_min_days, run_min_days
from solution import Solution

# %%
# Example test case
n = 10
expected = 4

# %%
result = run_min_days(Solution, n)
result

# %%
assert_min_days(result, expected)
