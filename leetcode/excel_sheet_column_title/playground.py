# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_convert_to_title, run_convert_to_title
from solution import Solution

# %%
# Example test case
column_number = 28
expected = "AB"

# %%
result = run_convert_to_title(Solution, column_number)
result

# %%
assert_convert_to_title(result, expected)
