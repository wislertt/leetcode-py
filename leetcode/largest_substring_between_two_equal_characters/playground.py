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
from helpers import (
    assert_max_length_between_equal_characters,
    run_max_length_between_equal_characters,
)
from solution import Solution

# %%
# Example test case
s = "abca"
expected = 2

# %%
result = run_max_length_between_equal_characters(Solution, s)
result

# %%
assert_max_length_between_equal_characters(result, expected)
