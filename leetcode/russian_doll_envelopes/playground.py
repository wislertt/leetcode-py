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
from helpers import assert_max_envelopes, run_max_envelopes
from solution import Solution

# %%
# Example test case
envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
expected = 3

# %%
result = run_max_envelopes(Solution, envelopes)
result

# %%
assert_max_envelopes(result, expected)
