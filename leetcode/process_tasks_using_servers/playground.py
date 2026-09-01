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
from helpers import assert_assign_tasks, run_assign_tasks
from solution import Solution

# %%
# Example test case
servers = [3, 3, 2]
tasks = [1, 2, 3, 2, 1, 2]
expected = [2, 2, 0, 2, 1, 2]

# %%
result = run_assign_tasks(Solution, servers, tasks)
result

# %%
assert_assign_tasks(result, expected)
