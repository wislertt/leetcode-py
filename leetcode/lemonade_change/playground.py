# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_lemonade_change, run_lemonade_change
from solution import Solution

# %%
# Example test case
bills = [5, 5, 5, 10, 20]
expected = True

# %%
result = run_lemonade_change(Solution, bills)
result

# %%
assert_lemonade_change(result, expected)
