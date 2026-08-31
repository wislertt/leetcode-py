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
from helpers import assert_group_strings, run_group_strings
from solution import Solution

# %%
# Example test case
strings = ["abc", "bcd"]
expected = [["abc", "bcd"]]

# %%
result = run_group_strings(Solution, strings)
result

# %%
assert_group_strings(result, expected)
