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
from helpers import assert_file_system, run_file_system
from solution import FileSystem

# %%
# Example test case
operations = ["FileSystem", "createPath", "get"]
inputs = [[], ["/a", 1], ["/a"]]
expected = [None, True, 1]

# %%
result, fs = run_file_system(FileSystem, operations, inputs)
print(result)
fs

# %%
assert_file_system(result, expected)
