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
from helpers import assert_number_of_beams, run_number_of_beams
from solution import Solution

# %%
# Example test case
bank = ["011001", "000000", "010100", "001000"]
expected = 8

# %%
result = run_number_of_beams(Solution, bank)
result

# %%
assert_number_of_beams(result, expected)
