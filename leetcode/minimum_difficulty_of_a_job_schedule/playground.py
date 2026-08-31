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
from helpers import assert_min_difficulty, run_min_difficulty
from solution import Solution

# %%
# Example test case
job_difficulty = [6, 5, 4, 3, 2, 1]
d = 2
expected = 7

# %%
result = run_min_difficulty(Solution, job_difficulty, d)
result

# %%
assert_min_difficulty(result, expected)
