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
from helpers import assert_deck_revealed_increasing, run_deck_revealed_increasing
from solution import Solution

# %%
# Example test case
deck = [17, 13, 11, 2, 3, 5, 7]
expected = [2, 13, 3, 11, 5, 17, 7]

# %%
result = run_deck_revealed_increasing(Solution, deck)
result

# %%
assert_deck_revealed_increasing(result, expected)
