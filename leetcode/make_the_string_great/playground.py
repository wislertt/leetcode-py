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
from helpers import assert_make_good, run_make_good
from solution import Solution

# %%
# Example test case
s = "leEeetcode"
expected = "leetcode"

# %%
result = run_make_good(Solution, s)
result

# %%
assert_make_good(result, expected)
