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
from helpers import assert_shifting_letters, run_shifting_letters
from solution import Solution

# %%
# Example test case
s = "abc"
shifts = [3, 5, 9]
expected = "rpl"

# %%
result = run_shifting_letters(Solution, s, shifts)
result

# %%
assert_shifting_letters(result, expected)
