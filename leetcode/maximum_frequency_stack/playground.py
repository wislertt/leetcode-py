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
from helpers import assert_freq_stack_operations, run_freq_stack_operations
from solution import FreqStack

# %%
# Example test case
operations = [
    "FreqStack",
    "push",
    "push",
    "push",
    "push",
    "push",
    "push",
    "pop",
    "pop",
    "pop",
    "pop",
]
inputs = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
expected = [None, None, None, None, None, None, None, 5, 7, 5, 4]

# %%
result = run_freq_stack_operations(FreqStack, operations, inputs)
result

# %%
assert_freq_stack_operations(result, expected)
