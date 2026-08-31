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
from helpers import assert_distribute_coins, run_distribute_coins
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 0, 0]
expected = 2

# %%
result = run_distribute_coins(Solution, root_list)
result

# %%
assert_distribute_coins(result, expected)
