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
from helpers import assert_autocomplete_system, run_autocomplete_system
from solution import AutocompleteSystem

# %%
# Example test case
operations = ["AutocompleteSystem", "input", "input", "input", "input"]
inputs = [
    [["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]],
    ["i"],
    [" "],
    ["a"],
    ["#"],
]
expected = [
    None,
    ["i love you", "island", "i love leetcode"],
    ["i love you", "i love leetcode"],
    [],
    [],
]

# %%
result, system = run_autocomplete_system(AutocompleteSystem, operations, inputs)
print(result)
system

# %%
assert_autocomplete_system(result, expected)
