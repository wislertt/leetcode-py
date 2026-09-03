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
from helpers import assert_shortest_path_all_keys, run_shortest_path_all_keys
from solution import Solution

# %%
# Example test case
grid = ["@.a..", "###.#", "b.A.B"]
expected = 8

# %%
result = run_shortest_path_all_keys(Solution, grid)
result

# %%
assert_shortest_path_all_keys(result, expected)
