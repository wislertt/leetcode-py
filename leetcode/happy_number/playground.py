# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_is_happy, run_is_happy
from solution import Solution

# %%
# Example test case
n = 19
expected = True

# %%
result = run_is_happy(Solution, n)
result

# %%
assert_is_happy(result, expected)
