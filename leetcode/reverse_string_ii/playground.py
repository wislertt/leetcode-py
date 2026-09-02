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
from helpers import assert_reverse_str, run_reverse_str
from solution import Solution

# %%
# Example test case
s = "abcdefg"
k = 2
expected = "bacdfeg"

# %%
result = run_reverse_str(Solution, s, k)
result

# %%
assert_reverse_str(result, expected)
