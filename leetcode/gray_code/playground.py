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
from helpers import assert_gray_code, run_gray_code
from solution import Solution

# %%
# Example test case
n = 2
expected_size = 4

# %%
result = run_gray_code(Solution, n)
result

# %%
assert_gray_code(result, expected_size)
