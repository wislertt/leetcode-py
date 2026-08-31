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
from helpers import assert_all_possible_fbt, run_all_possible_fbt
from solution import Solution

# %%
# Example test case
n = 5
expected = [[0, 0, 0, None, None, 0, 0], [0, 0, 0, 0, 0]]

# %%
result = run_all_possible_fbt(Solution, n)
result

# %%
assert_all_possible_fbt(result, expected)
