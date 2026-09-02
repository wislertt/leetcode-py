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
from helpers import assert_rand10, run_rand10
from solution import Solution

# %%
# Example test case
seed = 42
n = 20
expected = 20

# %%
values, calls = run_rand10(Solution, seed, n)
print(values)
calls

# %%
assert_rand10((values, calls), expected)
