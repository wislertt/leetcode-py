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
from helpers import assert_is_power_of_four, run_is_power_of_four
from solution import Solution

# %%
# Example test case
n = 16
expected = True

# %%
result = run_is_power_of_four(Solution, n)
result

# %%
assert_is_power_of_four(result, expected)
