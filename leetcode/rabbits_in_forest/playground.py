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
from helpers import assert_num_rabbits, run_num_rabbits
from solution import Solution

# %%
# Example test case
answers = [1, 1, 2]
expected = 5

# %%
result = run_num_rabbits(Solution, answers)
result

# %%
assert_num_rabbits(result, expected)
