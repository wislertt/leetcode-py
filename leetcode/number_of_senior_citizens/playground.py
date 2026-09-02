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
from helpers import assert_count_seniors, run_count_seniors
from solution import Solution

# %%
# Example test case
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
expected = 2

# %%
result = run_count_seniors(Solution, details)
result

# %%
assert_count_seniors(result, expected)
