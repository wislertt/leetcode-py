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
from helpers import assert_nth_magical_number, run_nth_magical_number
from solution import Solution

# %%
# Example test case
n = 4
a = 2
b = 3
expected = 6

# %%
result = run_nth_magical_number(Solution, n, a, b)
result

# %%
assert_nth_magical_number(result, expected)
