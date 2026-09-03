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
from helpers import assert_max_dist_to_closest, run_max_dist_to_closest
from solution import Solution

# %%
# Example test case
seats = [1, 0, 0, 0, 1, 0, 1]
expected = 2

# %%
result = run_max_dist_to_closest(Solution, seats)
result

# %%
assert_max_dist_to_closest(result, expected)
