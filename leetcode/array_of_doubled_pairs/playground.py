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
from helpers import assert_can_reorder_doubled, run_can_reorder_doubled
from solution import Solution

# %%
# Example test case
arr = [3, 1, 3, 6]
expected = False

# %%
result = run_can_reorder_doubled(Solution, arr)
result

# %%
assert_can_reorder_doubled(result, expected)
