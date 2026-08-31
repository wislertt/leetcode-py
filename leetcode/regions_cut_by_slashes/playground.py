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
from helpers import assert_regions_by_slashes, run_regions_by_slashes
from solution import Solution

# %%
# Example test case
grid = [" /", "/ "]
expected = 2

# %%
result = run_regions_by_slashes(Solution, grid)
result

# %%
assert_regions_by_slashes(result, expected)
