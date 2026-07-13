# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_integer_break, run_integer_break
from solution import Solution

# %%
# Example test case
n = 10
expected = 36

# %%
result = run_integer_break(Solution, n)
result

# %%
assert_integer_break(result, expected)
