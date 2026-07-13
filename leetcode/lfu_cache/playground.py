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
from helpers import assert_lfu_cache, run_lfu_cache
from solution import LFUCache

# %%
# Example test case (operations, inputs, expected outputs)
operations = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
expected = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]

# %%
result, cache = run_lfu_cache(LFUCache, operations, inputs)
print(result)
cache

# %%
assert_lfu_cache(result, expected)
