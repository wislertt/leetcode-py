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
from helpers import assert_check_powers_of_three, run_check_powers_of_three
from solution import Solution

# %%
# Example test case
n = 12
expected = True

# %%
result = run_check_powers_of_three(Solution, n)
result

# %%
assert_check_powers_of_three(result, expected)
