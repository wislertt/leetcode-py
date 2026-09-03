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
from helpers import assert_to_lower_case, run_to_lower_case
from solution import Solution

# %%
# Example test case
s = "Hello"
expected = "hello"

# %%
result = run_to_lower_case(Solution, s)
result

# %%
assert_to_lower_case(result, expected)
