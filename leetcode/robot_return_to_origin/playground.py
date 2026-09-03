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
from helpers import assert_judge_circle, run_judge_circle
from solution import Solution

# %%
# Example test case
moves = "UD"
expected = True

# %%
result = run_judge_circle(Solution, moves)
result

# %%
assert_judge_circle(result, expected)
