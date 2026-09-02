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
from helpers import assert_magical_string, run_magical_string
from solution import Solution

# %%
# Example test case
n: int = 6
expected: int = 3

# %%
result = run_magical_string(Solution, n)
result

# %%
assert_magical_string(result, expected)
