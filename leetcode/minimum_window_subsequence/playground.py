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
from helpers import assert_min_window, run_min_window
from solution import Solution

# %%
# Example test case
s1 = "abcdebdde"
s2 = "bde"
expected = "bcde"

# %%
result = run_min_window(Solution, s1, s2)
result

# %%
assert_min_window(result, expected)
