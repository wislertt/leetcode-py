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
from helpers import assert_similar_rgb, run_similar_rgb
from solution import Solution

# %%
# Example test case
color = "#09f166"
expected = "#11ee66"

# %%
result = run_similar_rgb(Solution, color)
result

# %%
assert_similar_rgb(result, expected)
