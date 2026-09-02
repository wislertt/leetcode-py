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
from helpers import assert_does_valid_array_exist, run_does_valid_array_exist
from solution import Solution

# %%
# Example test case
derived = [1, 1, 0]
expected = True

# %%
result = run_does_valid_array_exist(Solution, derived)
result

# %%
assert_does_valid_array_exist(result, expected)
