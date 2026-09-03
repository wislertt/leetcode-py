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
from helpers import assert_is_one_bit_character, run_is_one_bit_character
from solution import Solution

# %%
# Example test case
bits = [1, 0, 0]
expected = True

# %%
result = run_is_one_bit_character(Solution, bits)
result

# %%
assert_is_one_bit_character(result, expected)
