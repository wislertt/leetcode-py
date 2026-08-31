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
from helpers import assert_shortest_way, run_shortest_way
from solution import Solution

# %%
# Example test case
source = "abc"
target = "abcbc"
expected = 2

# %%
result = run_shortest_way(Solution, source, target)
result

# %%
assert_shortest_way(result, expected)
