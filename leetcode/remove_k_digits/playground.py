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
from helpers import assert_remove_k_digits, run_remove_k_digits
from solution import Solution

# %%
# Example test case
num = "1432219"
k = 3
expected = "1219"

# %%
result = run_remove_k_digits(Solution, num, k)
result

# %%
assert_remove_k_digits(result, expected)
