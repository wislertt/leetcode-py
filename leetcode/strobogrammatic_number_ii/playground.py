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
from helpers import assert_find_strobogrammatic, run_find_strobogrammatic
from solution import Solution

# %%
# Example test case
n = 2
expected = ["11", "69", "88", "96"]

# %%
result = run_find_strobogrammatic(Solution, n)
result

# %%
assert_find_strobogrammatic(result, expected)
