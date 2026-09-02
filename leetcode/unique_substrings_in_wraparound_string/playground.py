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
    assert_find_substring_in_wrapround_string,
    run_find_substring_in_wrapround_string,
)
from solution import Solution

# %%
# Example test case
s = "zab"
expected = 6

# %%
result = run_find_substring_in_wrapround_string(Solution, s)
result

# %%
assert_find_substring_in_wrapround_string(result, expected)
