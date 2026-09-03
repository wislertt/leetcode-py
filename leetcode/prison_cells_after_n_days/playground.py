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
from helpers import assert_prison_after_n_days, run_prison_after_n_days
from solution import Solution

# %%
# Example test case
cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 7
expected = [0, 0, 1, 1, 0, 0, 0, 0]

# %%
result = run_prison_after_n_days(Solution, cells, n)
result

# %%
assert_prison_after_n_days(result, expected)
