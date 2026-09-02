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
from helpers import assert_largest_good_integer, run_largest_good_integer
from solution import Solution

# %%
# Example test case
num = "6777133339"
expected = "777"

# %%
result = run_largest_good_integer(Solution, num)
result

# %%
assert_largest_good_integer(result, expected)
