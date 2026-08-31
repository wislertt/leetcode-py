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
from helpers import assert_smallest_factorization, run_smallest_factorization
from solution import Solution

# %%
# Example test case
num = 48
expected = 68

# %%
result = run_smallest_factorization(Solution, num)
result

# %%
assert_smallest_factorization(result, expected)
