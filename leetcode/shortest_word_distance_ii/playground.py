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
from helpers import assert_shortest_word_distance_ii, run_shortest_word_distance_ii
from solution import WordDistance

# %%
# Example test case
operations = ["WordDistance", "shortest", "shortest"]
inputs = [
    ["practice", "makes", "perfect", "coding", "makes"],
    ["coding", "practice"],
    ["makes", "coding"],
]
expected = [None, 3, 1]

# %%
result, distance = run_shortest_word_distance_ii(WordDistance, operations, inputs)
result

# %%
assert_shortest_word_distance_ii(result, expected)
