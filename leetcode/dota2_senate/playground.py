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
from helpers import assert_predict_party_victory, run_predict_party_victory
from solution import Solution

# %%
# Example test case
senate = "RD"
expected = "Radiant"

# %%
result = run_predict_party_victory(Solution, senate)
result

# %%
assert_predict_party_victory(result, expected)
