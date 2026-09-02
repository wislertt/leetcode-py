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
from helpers import assert_count_days, run_count_days
from solution import Solution

# %%
# Example test case
days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
expected = 2

# %%
result = run_count_days(Solution, days, meetings)
result

# %%
assert_count_days(result, expected)
