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
from helpers import assert_pair_sum, run_pair_sum
from solution import Solution

# %%
# Example test case
head_list: list[int] = [5, 4, 2, 1]
expected = 6

# %%
result = run_pair_sum(Solution, head_list)
result

# %%
assert_pair_sum(result, expected)
