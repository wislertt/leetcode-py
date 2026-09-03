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
from helpers import assert_next_greatest_letter, run_next_greatest_letter
from solution import Solution

# %%
# Example test case
letters: list[str] = ["c", "f", "j"]
target = "a"
expected = "c"

# %%
result = run_next_greatest_letter(Solution, letters, target)
result

# %%
assert_next_greatest_letter(result, expected)
