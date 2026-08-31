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
from helpers import assert_lexical_order, run_lexical_order
from solution import Solution

# %%
# Example test case
n = 13
expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

# %%
result = run_lexical_order(Solution, n)
result

# %%
assert_lexical_order(result, expected)
