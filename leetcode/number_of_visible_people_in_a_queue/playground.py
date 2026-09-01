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
from helpers import assert_can_see_persons_count, run_can_see_persons_count
from solution import Solution

# %%
# Example test case
heights = [10, 6, 8, 5, 11, 9]
expected = [3, 1, 2, 1, 1, 0]

# %%
result = run_can_see_persons_count(Solution, heights)
result

# %%
assert_can_see_persons_count(result, expected)
