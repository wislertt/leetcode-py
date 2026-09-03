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
from helpers import assert_reordered_power_of_2, run_reordered_power_of_2
from solution import Solution

# %%
# Example test case
n = 1
expected = True

# %%
result = run_reordered_power_of_2(Solution, n)
result

# %%
assert_reordered_power_of_2(result, expected)
