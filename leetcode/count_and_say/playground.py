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
from helpers import assert_count_and_say, run_count_and_say
from solution import Solution

# %%
# Example test case
n = 4
expected = "1211"

# %%
result = run_count_and_say(Solution, n)
result

# %%
assert_count_and_say(result, expected)
