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
from helpers import assert_remove_stars, run_remove_stars
from solution import Solution

# %%
# Example test case
s = "leet**cod*e"
expected = "lecoe"

# %%
result = run_remove_stars(Solution, s)
result

# %%
assert_remove_stars(result, expected)
