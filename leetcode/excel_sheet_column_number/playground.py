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
from helpers import assert_title_to_number, run_title_to_number
from solution import Solution

# %%
# Example test case
column_title = "AB"
expected = 28

# %%
result = run_title_to_number(Solution, column_title)
result

# %%
assert_title_to_number(result, expected)
