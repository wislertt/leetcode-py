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
from helpers import assert_guess_majority, run_guess_majority
from solution import Solution

# %%
# Example test case
nums = [0, 0, 1, 0, 1, 1, 1, 1]
expected = 5

# %%
result = run_guess_majority(Solution, nums)
result

# %%
assert_guess_majority(result, expected, nums)
