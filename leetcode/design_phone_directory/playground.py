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
from helpers import assert_phone_directory, run_phone_directory
from solution import PhoneDirectory

# %%
# Example test case
operations = ["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
inputs = [[3], [], [], [2], [], [2], [2], [2]]
expected = [None, 0, 1, True, 2, False, None, True]

# %%
result, directory = run_phone_directory(PhoneDirectory, operations, inputs)
print(result)
directory

# %%
assert_phone_directory(result, expected)
