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
from helpers import assert_strong_password_checker, run_strong_password_checker
from solution import Solution

# %%
# Example test case
password = "a"
expected = 5

# %%
result = run_strong_password_checker(Solution, password)
result

# %%
assert_strong_password_checker(result, expected)
