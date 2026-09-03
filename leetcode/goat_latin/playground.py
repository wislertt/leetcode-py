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
from helpers import assert_to_goat_latin, run_to_goat_latin
from solution import Solution

# %%
# Example test case
sentence = "I speak Goat Latin"
expected = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

# %%
result = run_to_goat_latin(Solution, sentence)
result

# %%
assert_to_goat_latin(result, expected)
