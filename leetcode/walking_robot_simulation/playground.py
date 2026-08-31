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
from helpers import assert_robot_sim, run_robot_sim
from solution import Solution

# %%
# Example test case
commands = [4, -1, 4, -2, 4]
obstacles = [[2, 4]]
expected = 65

# %%
result = run_robot_sim(Solution, commands, obstacles)
result

# %%
assert_robot_sim(result, expected)
