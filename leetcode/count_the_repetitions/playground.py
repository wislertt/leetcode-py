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
from helpers import assert_get_max_repetitions, run_get_max_repetitions
from solution import Solution

# %%
# Example test case
s1 = "acb"
n1 = 4
s2 = "ab"
n2 = 2
expected = 2

# %%
result = run_get_max_repetitions(Solution, s1, n1, s2, n2)
result

# %%
assert_get_max_repetitions(result, expected)
