# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_is_alien_sorted, run_is_alien_sorted
from solution import Solution

# %%
# Example test case
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
expected = True

# %%
result = run_is_alien_sorted(Solution, words, order)
result

# %%
assert_is_alien_sorted(result, expected)
