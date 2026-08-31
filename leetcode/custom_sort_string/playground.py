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
from helpers import assert_custom_sort_string, run_custom_sort_string
from solution import Solution

# %%
# Example test case
order = "cba"
s = "abcd"
expected = "cbad"

# %%
result = run_custom_sort_string(Solution, order, s)
result

# %%
assert_custom_sort_string(result, expected)
