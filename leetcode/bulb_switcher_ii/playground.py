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
from helpers import assert_flip_lights, run_flip_lights
from solution import Solution

# %%
# Example test case
n = 1
presses = 1
expected = 2

# %%
result = run_flip_lights(Solution, n, presses)
result

# %%
assert_flip_lights(result, expected)
