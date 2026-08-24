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
from helpers import assert_int_to_roman, run_int_to_roman
from solution import Solution

# %%
# Example test case
num = 3749
expected = "MMMDCCXLIX"

# %%
result = run_int_to_roman(Solution, num)
result

# %%
assert_int_to_roman(result, expected)
