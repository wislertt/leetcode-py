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
from helpers import assert_min_steps, run_min_steps
from solution import Solution

# %%
# Example test case
n = 3
expected = 3

# %%
result = run_min_steps(Solution, n)
result

# %%
assert_min_steps(result, expected)
