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
from helpers import assert_add_to_array_form, run_add_to_array_form
from solution import Solution

# %%
# Example test case
num = [1, 2, 0, 0]
k = 34
expected = [1, 2, 3, 4]

# %%
result = run_add_to_array_form(Solution, num, k)
result

# %%
assert_add_to_array_form(result, expected)
