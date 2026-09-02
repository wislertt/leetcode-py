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
from helpers import assert_detect_capital_use, run_detect_capital_use
from solution import Solution

# %%
# Example test case
word = "USA"
expected = True

# %%
result = run_detect_capital_use(Solution, word)
result

# %%
assert_detect_capital_use(result, expected)
