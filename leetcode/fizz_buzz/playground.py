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
from helpers import assert_fizz_buzz, run_fizz_buzz
from solution import Solution

# %%
# Example test case
n = 5
expected = ["1", "2", "Fizz", "4", "Buzz"]

# %%
result = run_fizz_buzz(Solution, n)
result

# %%
assert_fizz_buzz(result, expected)
