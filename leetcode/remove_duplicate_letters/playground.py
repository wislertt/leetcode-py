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
from helpers import assert_remove_duplicate_letters, run_remove_duplicate_letters
from solution import Solution

# %%
# Example test case
s = "cbacdcbc"
expected = "acdb"

# %%
result = run_remove_duplicate_letters(Solution, s)
result

# %%
assert_remove_duplicate_letters(result, expected)
