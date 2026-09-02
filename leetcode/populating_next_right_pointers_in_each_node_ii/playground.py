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
from helpers import assert_connect, run_connect
from solution import Solution

# %%
# Example test case
root_list: list[int | None] = [1, 2, 3, 4, 5, None, 7]
expected_list: list[int | None] = [1, None, 2, 3, None, 4, 5, 7, None]

# %%
result = run_connect(Solution, root_list)
result

# %%
assert_connect(result, expected_list)
