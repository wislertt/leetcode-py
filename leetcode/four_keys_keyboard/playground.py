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
from helpers import assert_max_a, run_max_a
from solution import Solution

# %%
# Example test case
n = 7
expected = 9

# %%
result = run_max_a(Solution, n)
result

# %%
assert_max_a(result, expected)
