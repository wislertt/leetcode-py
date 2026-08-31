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
from helpers import assert_find_max_form, run_find_max_form
from solution import Solution

# %%
# Example test case
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
expected = 4

# %%
result = run_find_max_form(Solution, strs, m, n)
result

# %%
assert_find_max_form(result, expected)
