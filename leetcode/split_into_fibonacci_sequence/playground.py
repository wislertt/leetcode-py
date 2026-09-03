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
from helpers import assert_split_into_fibonacci, run_split_into_fibonacci
from solution import Solution

# %%
# Example test case
num = "1101111"
expected = [11, 0, 11, 11]

# %%
result = run_split_into_fibonacci(Solution, num)
result

# %%
assert_split_into_fibonacci(result, expected)
