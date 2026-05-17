# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_my_atoi, run_my_atoi
from solution import Solution

# %%
# Example test case
s = "42"
expected = 42

# %%
result = run_my_atoi(Solution, s)
result

# %%
assert_my_atoi(result, expected)
