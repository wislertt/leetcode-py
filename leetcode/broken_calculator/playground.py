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
from helpers import assert_broken_calc, run_broken_calc
from solution import Solution

# %%
# Example test case
start_value = 2
target = 3
expected = 2

# %%
result = run_broken_calc(Solution, start_value, target)
result

# %%
assert_broken_calc(result, expected)
