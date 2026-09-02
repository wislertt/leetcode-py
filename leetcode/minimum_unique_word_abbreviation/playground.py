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
from helpers import assert_min_abbreviation, run_min_abbreviation
from solution import Solution

# %%
# Example test case
target = "apple"
dictionary = ["blade"]

# %%
result = run_min_abbreviation(Solution, target, dictionary)
result

# %%
assert_min_abbreviation(result, target, dictionary)
