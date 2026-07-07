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
from helpers import assert_check_valid_string, run_check_valid_string
from solution import Solution

# %%
# Example test case
s = "(*)"
expected = True

# %%
result = run_check_valid_string(Solution, s)
result

# %%
assert_check_valid_string(result, expected)
