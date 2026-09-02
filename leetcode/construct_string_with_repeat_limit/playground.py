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
from helpers import assert_repeat_limited_string, run_repeat_limited_string
from solution import Solution

# %%
# Example test case
s = "cczazcc"
repeat_limit = 3
expected = "zzcccac"

# %%
result = run_repeat_limited_string(Solution, s, repeat_limit)
result

# %%
assert_repeat_limited_string(result, expected)
