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
from helpers import assert_smallest_number, run_smallest_number
from solution import Solution

# %%
# Example test case
pattern = "IIIDIDDD"
expected = "123549876"

# %%
result = run_smallest_number(Solution, pattern)
result

# %%
assert_smallest_number(result, expected)
