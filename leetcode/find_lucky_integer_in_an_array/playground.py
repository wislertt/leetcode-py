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
from helpers import assert_find_lucky, run_find_lucky
from solution import Solution

# %%
# Example test case
arr = [2, 2, 3, 4]
expected = 2

# %%
result = run_find_lucky(Solution, arr)
result

# %%
assert_find_lucky(result, expected)
