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
from helpers import assert_punishment_number, run_punishment_number
from solution import Solution

# %%
# Example test case
n = 10
expected = 182

# %%
result = run_punishment_number(Solution, n)
result

# %%
assert_punishment_number(result, expected)
