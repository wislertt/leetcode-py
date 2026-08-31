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
from helpers import assert_min_stickers, run_min_stickers
from solution import Solution

# %%
# Example test case
stickers = ["with", "example", "science"]
target = "thehat"
expected = 3

# %%
result = run_min_stickers(Solution, stickers, target)
result

# %%
assert_min_stickers(result, expected)
