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
from helpers import assert_predict_the_winner, run_predict_the_winner
from solution import Solution

# %%
# Example test case
nums = [1, 5, 233, 7]
expected = True

# %%
result = run_predict_the_winner(Solution, nums)
result

# %%
assert_predict_the_winner(result, expected)
