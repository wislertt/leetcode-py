# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_num_distinct, run_num_distinct
from solution import Solution

# %%
# Example test case
s = "rabbbit"
t = "rabbit"
expected = 3

# %%
result = run_num_distinct(Solution, s, t)
result

# %%
assert_num_distinct(result, expected)
