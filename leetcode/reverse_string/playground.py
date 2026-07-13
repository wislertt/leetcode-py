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
from helpers import assert_reverse_string, run_reverse_string
from solution import Solution

# %%
# Example test case
s = ["h", "e", "l", "l", "o"]
expected = ["o", "l", "l", "e", "h"]

# %%
result = run_reverse_string(Solution, s)
result

# %%
assert_reverse_string(result, expected)
