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
from helpers import assert_bulb_switch, run_bulb_switch
from solution import Solution

# %%
# Example test case
n: int = 3
expected: int = 1

# %%
result = run_bulb_switch(Solution, n)
result

# %%
assert_bulb_switch(result, expected)
