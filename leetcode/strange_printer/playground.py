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
from helpers import assert_strange_printer, run_strange_printer
from solution import Solution

# %%
# Example test case
s = "aaabbb"
expected = 2

# %%
result = run_strange_printer(Solution, s)
result

# %%
assert_strange_printer(result, expected)
