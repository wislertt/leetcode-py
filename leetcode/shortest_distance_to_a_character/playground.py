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
from helpers import assert_shortest_to_char, run_shortest_to_char
from solution import Solution

# %%
# Example test case
s = "loveleetcode"
c = "e"
expected = [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

# %%
result = run_shortest_to_char(Solution, s, c)
result

# %%
assert_shortest_to_char(result, expected)
