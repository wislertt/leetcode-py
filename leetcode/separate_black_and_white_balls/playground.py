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
from helpers import assert_minimum_steps, run_minimum_steps
from solution import Solution

# %%
# Example test case
s = "101"
expected = 1

# %%
result = run_minimum_steps(Solution, s)
result

# %%
assert_minimum_steps(result, expected)
