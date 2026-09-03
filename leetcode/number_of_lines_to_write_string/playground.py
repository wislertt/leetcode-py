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
from helpers import assert_number_of_lines, run_number_of_lines
from solution import Solution

# %%
# Example test case
widths = [10] * 26
s = "abcdefghijklmnopqrstuvwxyz"
expected = [3, 60]

# %%
result = run_number_of_lines(Solution, widths, s)
result

# %%
assert_number_of_lines(result, expected)
