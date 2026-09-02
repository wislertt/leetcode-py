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
from helpers import assert_min_depth, run_min_depth
from solution import Solution

# %%
# Example test case
root_list = [3, 9, 20, None, None, 15, 7]
expected = 2

# %%
result = run_min_depth(Solution, root_list)
result

# %%
assert_min_depth(result, expected)
