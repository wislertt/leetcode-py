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
from helpers import assert_makesquare, run_makesquare
from solution import Solution

# %%
# Example test case
matchsticks = [1, 1, 2, 2, 2]
expected = True

# %%
result = run_makesquare(Solution, matchsticks)
result

# %%
assert_makesquare(result, expected)
