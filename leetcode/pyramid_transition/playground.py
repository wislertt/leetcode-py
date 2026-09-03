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
from helpers import assert_pyramid_transition, run_pyramid_transition
from solution import Solution

# %%
# Example test case
bottom = "BCD"
allowed = ["BCC", "CDE", "CEA", "FFF"]
expected = True

# %%
result = run_pyramid_transition(Solution, bottom, allowed)
result

# %%
assert_pyramid_transition(result, expected)
