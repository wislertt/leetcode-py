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
from helpers import assert_max_score_sightseeing_pair, run_max_score_sightseeing_pair
from solution import Solution

# %%
# Example test case
values = [8, 1, 5, 2, 6]
expected = 11

# %%
result = run_max_score_sightseeing_pair(Solution, values)
result

# %%
assert_max_score_sightseeing_pair(result, expected)
