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
from helpers import assert_has_alternating_bits, run_has_alternating_bits
from solution import Solution

# %%
# Example test case
n = 5
expected = True

# %%
result = run_has_alternating_bits(Solution, n)
result

# %%
assert_has_alternating_bits(result, expected)
