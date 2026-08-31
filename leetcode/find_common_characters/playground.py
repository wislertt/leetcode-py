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
from helpers import assert_common_chars, run_common_chars
from solution import Solution

# %%
# Example test case
words = ["bella", "label", "roller"]
expected = ["e", "l", "l"]

# %%
result = run_common_chars(Solution, words)
result

# %%
assert_common_chars(result, expected)
