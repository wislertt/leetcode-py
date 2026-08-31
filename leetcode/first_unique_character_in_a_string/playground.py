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
from helpers import assert_first_uniq_char, run_first_uniq_char
from solution import Solution

# %%
# Example test case
s = "leetcode"
expected = 0

# %%
result = run_first_uniq_char(Solution, s)
result

# %%
assert_first_uniq_char(result, expected)
