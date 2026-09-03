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
from helpers import assert_shortest_completing_word, run_shortest_completing_word
from solution import Solution

# %%
# Example test case
license_plate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
expected = "steps"

# %%
result = run_shortest_completing_word(Solution, license_plate, words)
result

# %%
assert_shortest_completing_word(result, expected)
