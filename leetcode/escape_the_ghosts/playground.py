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
from helpers import assert_escape_ghosts, run_escape_ghosts
from solution import Solution

# %%
# Example test case
ghosts: list[list[int]] = [[1, 0], [0, 3]]
target: list[int] = [0, 1]
expected = True

# %%
result = run_escape_ghosts(Solution, ghosts, target)
result

# %%
assert_escape_ghosts(result, expected)
