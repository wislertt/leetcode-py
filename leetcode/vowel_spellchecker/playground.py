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
from helpers import assert_spellchecker, run_spellchecker
from solution import Solution

# %%
# Example test case
wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = ["kite", "Kite"]
expected = ["kite", "KiTe"]

# %%
result = run_spellchecker(Solution, wordlist, queries)
result

# %%
assert_spellchecker(result, expected)
