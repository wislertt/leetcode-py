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
from helpers import assert_max_killed_enemies, run_max_killed_enemies
from solution import Solution

# %%
# Example test case
grid: list[list[str]] = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
expected = 3

# %%
result = run_max_killed_enemies(Solution, grid)
result

# %%
assert_max_killed_enemies(result, expected)
