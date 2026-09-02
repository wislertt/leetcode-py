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
from helpers import assert_mini_parser, run_mini_parser
from solution import Solution

# %%
# Example test case
s = "324"
expected = 324

# %%
result = run_mini_parser(Solution, s)
result

# %%
assert_mini_parser(result, expected)
