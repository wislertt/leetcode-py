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
from helpers import assert_max_count, run_max_count
from solution import Solution

# %%
# Example test case
m = 3
n = 3
ops = [[2, 2], [3, 3]]
expected = 4

# %%
result = run_max_count(Solution, m, n, ops)
result

# %%
assert_max_count(result, expected)
