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
from helpers import assert_nth_ugly_number, run_nth_ugly_number
from solution import Solution

# %%
# Example test case
n = 10
expected = 12

# %%
result = run_nth_ugly_number(Solution, n)
result

# %%
assert_nth_ugly_number(result, expected)
