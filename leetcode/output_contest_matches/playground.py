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
from helpers import assert_find_contest_match, run_find_contest_match
from solution import Solution

# %%
# Example test case
n = 8
expected = "(((1,8),(4,5)),((2,7),(3,6)))"

# %%
result = run_find_contest_match(Solution, n)
result

# %%
assert_find_contest_match(result, n, expected)
