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
from helpers import assert_survived_robots_healths, run_survived_robots_healths
from solution import Solution

# %%
# Example test case
positions = [3, 5, 2, 6]
healths = [10, 10, 15, 12]
directions = "RLRL"
expected = [14]

# %%
result = run_survived_robots_healths(Solution, positions, healths, directions)
result

# %%
assert_survived_robots_healths(result, expected)
