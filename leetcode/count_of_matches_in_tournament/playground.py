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
from helpers import assert_number_of_matches, run_number_of_matches
from solution import Solution

# %%
# Example test case
n = 7
expected = 6

# %%
result = run_number_of_matches(Solution, n)
result

# %%
assert_number_of_matches(result, expected)
