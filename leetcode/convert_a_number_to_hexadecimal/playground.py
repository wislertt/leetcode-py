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
from helpers import assert_to_hex, run_to_hex
from solution import Solution

# %%
# Example test case
num = 26
expected = "1a"

# %%
result = run_to_hex(Solution, num)
result

# %%
assert_to_hex(result, expected)
