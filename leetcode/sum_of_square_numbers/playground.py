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
from helpers import assert_judge_square_sum, run_judge_square_sum
from solution import Solution

# %%
# Example test case
c = 5
expected = True

# %%
result = run_judge_square_sum(Solution, c)
result

# %%
assert_judge_square_sum(result, expected)
