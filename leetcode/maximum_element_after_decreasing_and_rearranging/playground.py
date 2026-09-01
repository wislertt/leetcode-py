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
from helpers import assert_maximum_element, run_maximum_element
from solution import Solution

# %%
# Example test case
arr = [2, 2, 1, 2, 1]
expected = 2

# %%
result = run_maximum_element(Solution, arr)
result

# %%
assert_maximum_element(result, expected)
