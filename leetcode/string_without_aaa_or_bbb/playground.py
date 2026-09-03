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
from helpers import assert_str_without3a3b, run_str_without3a3b
from solution import Solution

# %%
# Example test case
a = 1
b = 2
expected = 3

# %%
result = run_str_without3a3b(Solution, a, b)
result

# %%
assert_str_without3a3b(result, expected)
