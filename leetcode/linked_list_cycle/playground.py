# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_has_cycle, run_has_cycle
from solution import Solution

# %%
# Example test case
values = [3, 2, 0, -4]
pos = 1
expected = True

# %%
result = run_has_cycle(Solution, values, pos)
result

# %%
assert_has_cycle(result, expected)
