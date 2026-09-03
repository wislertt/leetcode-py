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
from helpers import assert_is_long_pressed_name, run_is_long_pressed_name
from solution import Solution

# %%
# Example test case
name = "alex"
typed = "aaleex"
expected = True

# %%
result = run_is_long_pressed_name(Solution, name, typed)
result

# %%
assert_is_long_pressed_name(result, expected)
