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
from helpers import assert_next_greater_element, run_next_greater_element
from solution import Solution

# %%
# Example test case
n = 12
expected = 21

# %%
result = run_next_greater_element(Solution, n)
result

# %%
assert_next_greater_element(result, expected)
