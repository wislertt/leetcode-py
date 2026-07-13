# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: leetcode-py-py3.13
#     language: python
#     name: python3
# ---

# %%
from helpers import assert_rob, run_rob
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [3, 2, 3, None, 3, None, 1]
expected = 7

# %%
result = run_rob(Solution, root_list)
result

# %%
assert_rob(result, expected)
