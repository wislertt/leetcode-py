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
from helpers import assert_minimized_maximum, run_minimized_maximum
from solution import Solution

# %%
# Example test case
n = 6
quantities = [11, 6]
expected = 3

# %%
result = run_minimized_maximum(Solution, n, quantities)
result

# %%
assert_minimized_maximum(result, expected)
