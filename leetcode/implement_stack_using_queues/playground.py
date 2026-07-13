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
from helpers import assert_my_stack, run_my_stack
from solution import MyStack

# %%
# Example test case
operations = ["MyStack", "push", "push", "top", "pop", "empty"]
inputs = [[], [1], [2], [], [], []]
expected = [None, None, None, 2, 2, False]

# %%
result, stack = run_my_stack(MyStack, operations, inputs)
print(result)
stack

# %%
assert_my_stack(result, expected)
