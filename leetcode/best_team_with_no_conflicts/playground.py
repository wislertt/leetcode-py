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
from helpers import assert_best_team_score, run_best_team_score
from solution import Solution

# %%
# Example test case
scores = [1, 3, 5, 10, 15]
ages = [1, 2, 3, 4, 5]
expected = 34

# %%
result = run_best_team_score(Solution, scores, ages)
result

# %%
assert_best_team_score(result, expected)
