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
from helpers import assert_candy, run_candy
from solution import Solution

# %%
# Example test case
ratings = [1, 0, 2]
expected = 5

# %%
result = run_candy(Solution, ratings)
result

# %%
assert_candy(result, expected)
