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
from helpers import assert_string_shift, run_string_shift
from solution import Solution

# %%
# Example test case
s = "abc"
shift = [[0, 1], [1, 2]]
expected = "cab"

# %%
result = run_string_shift(Solution, s, shift)
result

# %%
assert_string_shift(result, expected)
