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
from helpers import assert_get_hint, run_get_hint
from solution import Solution

# %%
# Example test case
secret = "1807"
guess = "7810"
expected = "1A3B"

# %%
result = run_get_hint(Solution, secret, guess)
result

# %%
assert_get_hint(result, expected)
