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
from helpers import assert_max_stack, run_max_stack
from solution import MaxStack

# %%
# Example test case
operations = ["MaxStack", "push", "push", "push", "top", "pop_max", "top", "peek_max", "pop", "top"]
inputs = [[], [5], [1], [5], [], [], [], [], [], []]
expected = [None, None, None, None, 5, 5, 1, 5, 1, 5]

# %%
result, stack = run_max_stack(MaxStack, operations, inputs)
print(result)
stack

# %%
assert_max_stack(result, expected)
