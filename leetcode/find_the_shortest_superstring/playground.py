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
from helpers import assert_shortest_superstring, run_shortest_superstring
from solution import Solution

# %%
# Example test case
words = ["alex", "loves", "leetcode"]
expected = 17

# %%
result = run_shortest_superstring(Solution, words)
result

# %%
assert_shortest_superstring(result, expected)
