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
from helpers import assert_check_record, run_check_record
from solution import Solution

# %%
# Example test case
n = 2
expected = 8

# %%
result = run_check_record(Solution, n)
result

# %%
assert_check_record(result, expected)
