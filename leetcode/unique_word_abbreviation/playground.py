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
from helpers import assert_valid_word_abbr, run_valid_word_abbr
from solution import ValidWordAbbr

# %%
# Example test case
operations = ["ValidWordAbbr", "is_unique", "is_unique", "is_unique"]
inputs = [["deer", "door", "cake", "card"], ["dear"], ["cart"], ["cane"]]
expected = [None, False, True, False]

# %%
result, implementation = run_valid_word_abbr(ValidWordAbbr, operations, inputs)
print(result)
implementation

# %%
assert_valid_word_abbr(result, expected)
