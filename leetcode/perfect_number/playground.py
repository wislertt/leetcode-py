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
from helpers import assert_check_perfect_number, run_check_perfect_number
from solution import Solution

# %%
# Example test case
num = 28
expected = True

# %%
result = run_check_perfect_number(Solution, num)
result

# %%
assert_check_perfect_number(result, expected)
