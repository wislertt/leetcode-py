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
from helpers import assert_ambiguous_coordinates, run_ambiguous_coordinates
from solution import Solution

# %%
# Example test case
s = "(123)"
expected = ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]

# %%
result = run_ambiguous_coordinates(Solution, s)
result

# %%
assert_ambiguous_coordinates(result, expected)
