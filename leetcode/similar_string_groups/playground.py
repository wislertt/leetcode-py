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
from helpers import assert_num_similar_groups, run_num_similar_groups
from solution import Solution

# %%
# Example test case
strs = ["tars", "rats", "arts", "star"]
expected = 2

# %%
result = run_num_similar_groups(Solution, strs)
result

# %%
assert_num_similar_groups(result, expected)
