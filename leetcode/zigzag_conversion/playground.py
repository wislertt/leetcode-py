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
from helpers import assert_convert, run_convert
from solution import Solution

# %%
# Example test case
s = "PAYPALISHIRING"
num_rows = 3
expected = "PAHNAPLSIIGYIR"

# %%
result = run_convert(Solution, s, num_rows)
result

# %%
assert_convert(result, expected)
