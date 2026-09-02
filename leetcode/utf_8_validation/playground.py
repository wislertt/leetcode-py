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
from helpers import assert_valid_utf8, run_valid_utf8
from solution import Solution

# %%
# Example test case
data = [197, 130, 1]
expected = True

# %%
result = run_valid_utf8(Solution, data)
result

# %%
assert_valid_utf8(result, expected)
