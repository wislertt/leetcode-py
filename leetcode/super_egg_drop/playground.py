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
from helpers import assert_super_egg_drop, run_super_egg_drop
from solution import Solution

# %%
# Example test case
k = 2
n = 6
expected = 3

# %%
result = run_super_egg_drop(Solution, k, n)
result

# %%
assert_super_egg_drop(result, expected)
