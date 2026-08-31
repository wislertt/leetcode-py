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
from helpers import assert_count_servers, run_count_servers
from solution import Solution

# %%
# Example test case
grid = [[1, 0], [1, 1]]
expected = 3

# %%
result = run_count_servers(Solution, grid)
result

# %%
assert_count_servers(result, expected)
