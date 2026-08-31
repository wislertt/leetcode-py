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
from helpers import assert_number_of_patterns, run_number_of_patterns
from solution import Solution

# %%
# Example test case
m = 1
n = 2
expected = 65

# %%
result = run_number_of_patterns(Solution, m, n)
result

# %%
assert_number_of_patterns(result, expected)
