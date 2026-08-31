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
from helpers import assert_is_robot_bounded, run_is_robot_bounded
from solution import Solution

# %%
# Example test case
instructions = "GGLLGG"
expected = True

# %%
result = run_is_robot_bounded(Solution, instructions)
result

# %%
assert_is_robot_bounded(result, expected)
