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
from helpers import assert_magic_dictionary, run_magic_dictionary
from solution import MagicDictionary

# %%
# Example test case
operations = ["MagicDictionary", "build_dict", "search", "search", "search", "search"]
inputs = [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
expected = [None, None, False, True, False, False]

# %%
result, magic = run_magic_dictionary(MagicDictionary, operations, inputs)
print(result)
magic

# %%
assert_magic_dictionary(result, expected)
