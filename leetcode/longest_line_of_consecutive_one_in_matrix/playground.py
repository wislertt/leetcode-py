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
from helpers import assert_longest_line, run_longest_line
from solution import Solution

# %%
# Example test case
mat = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
expected = 3

# %%
result = run_longest_line(Solution, mat)
result

# %%
assert_longest_line(result, expected)
