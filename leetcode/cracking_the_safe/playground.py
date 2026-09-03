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
from helpers import assert_crack_safe, run_crack_safe
from solution import Solution

# %%
# Example test case
n = 2
k = 2
expected = (2, 2)

# %%
result = run_crack_safe(Solution, n, k)
result

# %%
assert_crack_safe(result, expected)
