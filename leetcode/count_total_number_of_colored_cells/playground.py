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
from helpers import assert_colored_cells, run_colored_cells
from solution import Solution

# %%
# Example test case
n = 3
expected = 13

# %%
result = run_colored_cells(Solution, n)
result

# %%
assert_colored_cells(result, expected)
