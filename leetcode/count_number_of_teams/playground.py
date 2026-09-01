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
from helpers import assert_num_teams, run_num_teams
from solution import Solution

# %%
# Example test case
rating = [2, 5, 3, 4, 1]
expected = 3

# %%
result = run_num_teams(Solution, rating)
result

# %%
assert_num_teams(result, expected)
