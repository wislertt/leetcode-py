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
from helpers import assert_cheapest_jump, run_cheapest_jump
from solution import Solution

# %%
# Example test case
coins = [1, 2, 4, -1, 2]
max_jump = 2
expected = [1, 3, 5]

# %%
result = run_cheapest_jump(Solution, coins, max_jump)
result

# %%
assert_cheapest_jump(result, expected)
