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
from helpers import assert_kill_process, run_kill_process
from solution import Solution

# %%
# Example test case
pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
expected = [5, 10]

# %%
result = run_kill_process(Solution, pid, ppid, kill)
result

# %%
assert_kill_process(result, expected)
