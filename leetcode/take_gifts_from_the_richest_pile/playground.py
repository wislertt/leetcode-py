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
from helpers import assert_pick_gifts, run_pick_gifts
from solution import Solution

# %%
# Example test case
gifts = [25, 64, 9, 4, 100]
k = 4
expected = 29

# %%
result = run_pick_gifts(Solution, gifts, k)
result

# %%
assert_pick_gifts(result, expected)
