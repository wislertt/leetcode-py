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
from helpers import assert_all_one, run_all_one
from solution import AllOne

# %%
# Example test case
operations = [
    "AllOne",
    "inc",
    "inc",
    "get_max_key",
    "get_min_key",
    "inc",
    "get_max_key",
    "get_min_key",
]
inputs = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
expected = [None, None, None, "hello", "hello", None, "hello", "leet"]

# %%
result, all_one = run_all_one(AllOne, operations, inputs)
print(result)
all_one

# %%
assert_all_one(result, expected)
