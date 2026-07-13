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
from helpers import assert_longest_happy_string, run_longest_happy_string
from solution import Solution

# %%
# Example test case
a = 1
b = 1
c = 7

# %%
result = run_longest_happy_string(Solution, a, b, c)
result

# %%
assert_longest_happy_string(result, a, b, c)
