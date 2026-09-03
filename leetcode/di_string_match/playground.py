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
from helpers import assert_di_string_match, run_di_string_match
from solution import Solution

# %%
# Example test case
s = "IDID"
expected = [0, 4, 1, 3, 2]

# %%
result = run_di_string_match(Solution, s)
result

# %%
assert_di_string_match(result, expected, s)
